from tkinter import messagebox
import gui.gui as gui
import core.system_utils as system_utils
import core.ai_client as ai_client

def update_system_info(tab):
    """
        Fetches system information and updates the System Monitor tab.
        Arguments:
        -tab -> takes the system monitor tab as the argument as the values to manipulate are saved as tab object's properties. This is done to not lose the variables created in the function when function ends.
        -returns -> Does not return anything. Simple uses the gui tab object to call its update methods passing it new values.
    """
    try:
        cpu_usage = system_utils.get_cpu_usage()
        ram_usage = system_utils.get_ram_usage()
        disk_usage = system_utils.get_disk_usage()
        gui.update_system_monitor_tab(tab, cpu_usage, ram_usage, disk_usage)
        tab.after(1000, update_system_info, tab)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update system info: {e}")

def update_process_list(tab):
    """Fetches the list of running processes and updates the Process Manager tab after every 5 seconds."""
    try:
        processes = system_utils.get_running_processes()
        gui.update_process_manager_tab(tab, processes)
        # Update every 5000 milliseconds (1 second = 1000 milliseconds)
        tab.after(5000, update_process_list, tab)  
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update process list: {e}")

def main():
    try:
        root = gui.create_main_window()
        system_monitor_tab, process_manager_tab, startup_manager_tab, ai_assistance_tab = gui.create_tabs(root)

        ai_client_instance = ai_client.AIClient()
        gui.create_system_monitor_tab(system_monitor_tab)
        gui.create_process_manager_tab(process_manager_tab)
        gui.create_startup_manager_tab(startup_manager_tab)
        gui.create_ai_assistance_tab( ai_assistance_tab, ai_client_instance)

        # Initial updates
        update_system_info(system_monitor_tab)
        update_process_list(process_manager_tab)

        # Ensures that the window remains open. Without this method, it opens and closes instantly.
        root.mainloop()

    except Exception as e:
        # Ensure window is closed if error occurs
        if root:
            root.destroy() 
        messagebox.showerror("Error", f"Application initialization failed: {e}")

if __name__ == "__main__":
    main()