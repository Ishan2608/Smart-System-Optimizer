import psutil
import platform

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
    """Returns a list of startup programs from Windows registry."""
    import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Run")
        i = 0
        programs = []
        while True:
            name, value, _ = winreg.EnumValue(key, i)
            programs.append(f"{name}: {value}")
            i += 1
    except OSError as e:
        print(f"Error accessing registry: {e}")  # Log error
        return []
    finally:
        try:
            winreg.CloseKey(key)
        except:
            pass
        return programs

def enable_startup_program(name, path):
    """
    Adds a program to the Windows startup registry.
    Args:
        name: Name of the program
        path: Full executable path of the program
    """
    import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"Software\Microsoft\Windows\CurrentVersion\Run",
                            0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, path)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"Error enabling startup: {e}")
        return False


def disable_startup_program(name):
    """
    Removes a program from the Windows startup registry.
    Args:
        name: Name of the program to remove
    """
    import winreg
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"Software\Microsoft\Windows\CurrentVersion\Run",
                            0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, name)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        print(f"Program '{name}' not found in startup.")
        return False
    except Exception as e:
        print(f"Error disabling startup: {e}")
        return False
    
