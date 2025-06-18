import psutil
import platform

# Global path cache to preserve paths across disable/enable
disabled_program_cache = {}

def get_cpu_usage(interval=0.1):  # 0.1 seconds interval
    """Returns the current CPU usage as a percentage."""
    return psutil.cpu_percent(interval=interval)

def get_ram_usage():
    """Returns the total and used RAM in GB."""
    ram = psutil.virtual_memory()
    total = ram.total / (1024 ** 3)  # Convert bytes to GB
    used = ram.used / (1024 ** 3) # Convert bytes to GB
    return total, used

def get_disk_usage():
    """Returns the total and used disk space for each partition."""
    disk_usage = []
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total = usage.total / (1024 ** 3)  # Convert bytes to GB
            used = usage.used / (1024 ** 3)
            disk_usage.append({
                "partition": partition.mountpoint,
                "total": total,
                "used": used
            })
        except PermissionError:
            # Handle cases where permission is denied to access a partition
            disk_usage.append({
                "partition": partition.mountpoint,
                "total": 0,
                "used": 0,
                "error": "PermissionError"
            })
    return disk_usage

def get_running_processes():
    """Returns a list of all running processes with details."""
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu_percent": proc.info['cpu_percent'],
                "memory_percent": proc.info['memory_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignore processes that have terminated or we can't access
            pass  
    return processes

def terminate_process(pid):
    """Terminates the process with the given PID."""
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait()  # Wait for the process to terminate
        return True
    except psutil.NoSuchProcess:
        return False  # Process already terminated
    except psutil.AccessDenied:
        return False  # Permission denied

def set_process_priority(pid, priority):
    """Sets the priority of the process with the given PID."""
    try:
        proc = psutil.Process(pid)
        if platform.system() == "Windows":
            if priority == "high":
                proc.nice(psutil.HIGH_PRIORITY_CLASS)
            elif priority == "above_normal":
                proc.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
            elif priority == "normal":
                proc.nice(psutil.NORMAL_PRIORITY_CLASS)
            elif priority == "below_normal":
                proc.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
            elif priority == "idle":
                proc.nice(psutil.IDLE_PRIORITY_CLASS)
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            if priority == "high":
                proc.nice(-10)  # Highest priority (requires root privileges)
            elif priority == "above_normal":
                proc.nice(-5)
            elif priority == "normal":
                proc.nice(0)
            elif priority == "below_normal":
                proc.nice(5)
            elif priority == "idle":
                proc.nice(19)  # Lowest priority
        return True
    except psutil.NoSuchProcess:
        return False
    except psutil.AccessDenied:
        return False

def get_startup_programs():
    """
    Returns a list of startup programs, both enabled and disabled,
    with their path and status, from both HKCU and HKLM.
    Falls back to cached path if available.
    """
    import winreg

    # Use the global cache
    global disabled_program_cache

    def read_run_key(root, path):
        """Reads enabled entries with paths from the Run key."""
        programs = {}
        try:
            with winreg.OpenKey(root, path) as key:
                i = 0
                while True:
                    name, value, _ = winreg.EnumValue(key, i)
                    programs[name] = value
                    i += 1
        except OSError:
            pass
        return programs

    def read_startup_approved_key(root, path):
        """Reads enabled/disabled status from StartupApproved."""
        status_map = {}
        try:
            with winreg.OpenKey(root, path) as key:
                i = 0
                while True:
                    name, data, _ = winreg.EnumValue(key, i)
                    # Byte[0] = 2 (enabled), 3 (disabled)
                    status_map[name] = "enabled" if data[0] == 2 else "disabled"
                    i += 1
        except OSError:
            pass
        return status_map

    # Step 1: Fetch paths from Run keys
    run_hkcu = read_run_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
    run_hklm = read_run_key(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")

    # Step 2: Fetch statuses from StartupApproved keys
    approved_hkcu = read_startup_approved_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run")
    approved_hklm = read_startup_approved_key(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run")

    # Step 3: Merge all unique program names from all sources
    all_programs = set(run_hkcu.keys()) | set(run_hklm.keys()) | set(approved_hkcu.keys()) | set(approved_hklm.keys())

    result = []

    for name in all_programs:
        # Determine path: prefer live registry, fallback to in-memory cache
        path = run_hkcu.get(name) or run_hklm.get(name) or disabled_program_cache.get(name) or "Path not available"

        # Determine status: prefer explicitly marked status, default to enabled
        status = approved_hkcu.get(name) or approved_hklm.get(name) or "enabled"

        result.append({
            "name": name,
            "path": path,
            "status": status
        })

    return result


def enable_startup_program(name, path, scope="user"):
    """
    Enables a startup program by writing to both Run and StartupApproved registry keys.
    Args:
        name: Name of the program
        path: Full executable path of the program
        scope: "user" or "machine"
    """
    import winreg
    try:
        root = winreg.HKEY_CURRENT_USER if scope == "user" else winreg.HKEY_LOCAL_MACHINE
        access = winreg.KEY_SET_VALUE
        if scope == "machine":
            access |= winreg.KEY_WOW64_64KEY

        # Step 1: Write to Run key
        run_key = winreg.OpenKey(
            root,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            access
        )
        winreg.SetValueEx(run_key, name, 0, winreg.REG_SZ, path)
        winreg.CloseKey(run_key)

        # Step 2: Write to StartupApproved to mark as enabled
        approved_key = winreg.OpenKey(
            root,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run",
            0,
            access
        )
        # Byte 0 = 2 = enabled
        winreg.SetValueEx(approved_key, name, 0, winreg.REG_BINARY, bytes([0x02, 0x00, 0x00, 0x00]))
        winreg.CloseKey(approved_key)

        return True
    except Exception as e:
        print(f"Error enabling startup: {e}")
        return False


def disable_startup_program(name):
    """
    Disables a startup program by removing it from Run and writing 'disabled' status to StartupApproved.
    Caches the path in-memory so it can still be shown in the UI.
    """
    import winreg
    removed = False

    for root in [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]:
        try:
            access = winreg.KEY_ALL_ACCESS
            if root == winreg.HKEY_LOCAL_MACHINE:
                access |= winreg.KEY_WOW64_64KEY

            key = winreg.OpenKey(root, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, access)

            try:
                path, _ = winreg.QueryValueEx(key, name)
                disabled_program_cache[name] = path  # Save path before deleting
                winreg.DeleteValue(key, name)
                removed = True
            except FileNotFoundError:
                pass
            winreg.CloseKey(key)

            # Mark it as disabled in StartupApproved
            approved_key = winreg.OpenKey(
                root,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run",
                0,
                access
            )
            winreg.SetValueEx(approved_key, name, 0, winreg.REG_BINARY, bytes([0x03, 0x00, 0x00, 0x00]))  # disabled
            winreg.CloseKey(approved_key)

        except Exception as e:
            print(f"[Disable] Error for {name} in registry: {e}")

    return removed
