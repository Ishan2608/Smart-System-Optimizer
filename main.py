from tkinter import messagebox
import gui.gui as gui
import core.ai_client as ai_client

def main():
    root = None
    try:

        root = gui.create_main_window()
        system_monitor_tab, process_manager_tab, startup_manager_tab, ai_assistance_tab = gui.create_tabs(root)
        ai_client_instance = ai_client.AIClient()

        gui.create_system_monitor_tab(system_monitor_tab)
        gui.create_process_manager_tab(process_manager_tab)
        gui.create_startup_manager_tab(startup_manager_tab)
        gui.create_ai_assistance_tab(ai_assistance_tab, ai_client_instance)

        root.mainloop()

    except Exception as e:
        if root:
            root.destroy()
        messagebox.showerror("Error", f"Application initialization failed: {e}")

if __name__ == "__main__":
    main()