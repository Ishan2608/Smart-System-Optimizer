import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
import threading
import core.system_utils as system_utils

def apply_dark_theme(root):
    """
    Applies a dark blue-gray theme to the entire application.
    
    Args:
        root: The main Tkinter window on which the style will be applied.
    """
    # Define colors
    bg_color = "#1E2430"
    fg_color = "#E0E0E0"
    accent_color = "#3A506B"
    highlight_color = "#5BC0BE"
    button_bg = "#2C3E50"
    
    # Font configurations - added font sizes and families
    normal_font = ("Arial", 12)
    header_font = ("Arial", 14, "bold")
    button_font = ("Arial", 12)
    
    # Configure ttk style
    style = ttk.Style()
    
    # Create theme
    style.theme_create("dark_theme", parent="alt", settings={
        "TFrame": {
            "configure": {"background": bg_color}
        },
        "TNotebook": {
            "configure": {"background": bg_color, "tabmargins": [2, 5, 2, 0]}
        },
        "TNotebook.Tab": {
            "configure": {
                "background": accent_color, 
                "foreground": fg_color,
                "padding": [10, 2],
                "font": header_font,
            },
            "map": {
                "background": [("selected", bg_color)],
                "foreground": [("selected", highlight_color)],
                "expand": [("selected", [1, 1, 1, 0])]
            }
        },
        "TLabel": {
            "configure": {
                "background": bg_color, 
                "foreground": fg_color,
                "font": normal_font
            }
        },
        "TButton": {
            "configure": {
                "background": button_bg, 
                "foreground": fg_color,
                "padding": [10, 5],
                "font": button_font
            },
            "map": {
                "background": [("active", highlight_color)],
                "foreground": [("active", bg_color)]
            }
        },
        "TEntry": {
            "configure": {
                "fieldbackground": accent_color,
                "foreground": fg_color,
                "insertcolor": fg_color,
                "padding": [5, 3],
                "font": normal_font
            }
        }
    })
    
    # Set the theme
    style.theme_use("dark_theme")
    
    # Configure colors for non-ttk widgets
    root.configure(background=bg_color)
    
    # Additional widget-specific configurations
    def configure_widgets(widget):
        widget_class = widget.winfo_class()
        
        if widget_class == "Text":
            widget.configure(
                background=accent_color,
                foreground=fg_color,
                insertbackground=fg_color,  # Cursor color
                selectbackground=highlight_color,
                selectforeground=bg_color,
                highlightthickness=1,
                highlightbackground=accent_color,
                highlightcolor=highlight_color,
                relief="flat",
                padx=5,
                pady=5,
                font=normal_font  # Added font configuration
            )
        elif widget_class == "Listbox":
            widget.configure(
                background=accent_color,
                foreground=fg_color,
                selectbackground=highlight_color,
                selectforeground=bg_color,
                highlightthickness=1,
                highlightbackground=accent_color,
                highlightcolor=highlight_color,
                relief="flat",
                font=normal_font  # Added font configuration
            )
        elif widget_class == "Label":
            widget.configure(
                background=bg_color,
                foreground=fg_color,
                font=normal_font  # Added font configuration
            )
        elif widget_class == "Button":
            widget.configure(
                background=button_bg,
                foreground=fg_color,
                activebackground=highlight_color,
                activeforeground=bg_color,
                font=button_font  # Added font configuration
            )
        elif widget_class == "Entry":
            widget.configure(
                background=accent_color,
                foreground=fg_color,
                insertbackground=fg_color,
                font=normal_font  # Added font configuration
            )
            
        # Apply to children recursively
        for child in widget.winfo_children():
            configure_widgets(child)
    
    # Apply configurations to all existing widgets
    configure_widgets(root)

def create_main_window():
    """Creates the main application window."""
    root = tk.Tk()
    root.title("Smart System Optimizer")
    root.geometry("800x600")
    apply_dark_theme(root)
    return root

def create_tabs(master):
    """Creates the notebook (tab) widget."""

    # Create a tabbed interface using Notebook() class. 
    # Pass it the variable that represents the main program window.
    notebook = ttk.Notebook(master)

    # Parent of ttk.Frame is notebook. Frame creates a screen to show in the program window.
    system_monitor_tab = ttk.Frame(notebook)
    process_manager_tab = ttk.Frame(notebook)
    startup_manager_tab = ttk.Frame(notebook)
    ai_assistance_tab = ttk.Frame(notebook)

    # Now that the tabs have been created separately, 
    # and we have specified the parent of each tab, we can add them to the notebook.
    notebook.add(system_monitor_tab, text="System Monitor")
    notebook.add(process_manager_tab, text="Process Manager")
    notebook.add(startup_manager_tab, text="Startup Manager")
    notebook.add(ai_assistance_tab, text="AI Assistance")


    # Pack ensures that the notebook is displayed in the main window.
    # The expand and fill options ensure that the notebook expands to fill the window when it is resized.
    notebook.pack(expand=True, fill='both')
    return (
        system_monitor_tab,
        process_manager_tab,
        startup_manager_tab,
        ai_assistance_tab,
    )

# -----------------------------------------------------------------------------
# System Monitor Tab
# -----------------------------------------------------------------------------

def create_system_monitor_tab(tab):
    """
        Creates the content for the System Monitor tab.
        Create 3 static labels, and create their respective labels to display CPU, RAM, and Disk usage.
        The labels should be aligned to the left and top of the tab.
        ---
        Arguments
        - `tab`: argument is the tab frame where the content will be placed. To ensure that the variables representing
        widgets are accessible outside the function, we store them as attributes of the `tab` frame.
    """
    # Labels to display system information
    cpu = ttk.Label(tab, text="CPU Usage:")
    cpu.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    cpu_label = ttk.Label(tab, text="N/A")
    cpu_label.grid(row=0, column=1, padx=50, pady=5, sticky="w")

    ram = ttk.Label(tab, text="RAM Usage:")
    ram.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    ram_label = ttk.Label(tab, text="N/A")
    ram_label.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    disk = ttk.Label(tab, text="Disk Usage:")
    disk.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
    disk_label = ttk.Label(tab, text="N/A")
    disk_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Store the labels in as properties of tabs so we can update them later outside the function.
    tab.cpu_label = cpu_label
    tab.ram_label = ram_label
    tab.disk_label = disk_label

    cpu_usage = system_utils.get_cpu_usage()
    ram_usage = system_utils.get_ram_usage()
    disk_usage = system_utils.get_disk_usage()

    # Update the labels with initial values
    update_system_monitor_tab(tab, cpu_usage, ram_usage, disk_usage)

def update_system_monitor_tab(tab, cpu_usage, ram_usage, disk_usage):
    """Updates the data displayed in the System Monitor tab."""
    tab.cpu_label.config(text=f"{cpu_usage}%")
    tab.ram_label.config(text=f"Total: {ram_usage[0]:.2f} GB, Used: {ram_usage[1]:.2f} GB")
    disk_text = ""
    for disk in disk_usage:
        disk_text += (
            f"{disk['partition']}: Total: {disk['total']:.2f} GB, Used: {disk['used']:.2f} GB\n"
        )
    tab.disk_label.config(text=disk_text)

    tab.after(1000, update_system_monitor_tab, tab, system_utils.get_cpu_usage(), system_utils.get_ram_usage(), system_utils.get_disk_usage())

# -----------------------------------------------------------------------------
# Process Manager Tab
# -----------------------------------------------------------------------------

def create_process_manager_tab(tab):
    """Creates the content for the Process Manager tab."""
    # Listbox to display processes
    process_listbox = tk.Listbox(tab)
    process_listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Buttons to manage processes
    terminate_button = ttk.Button(tab, text="Terminate Process")
    terminate_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    priority_button = ttk.Button(tab, text="Change Priority")
    priority_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")

   # Buttons to manage processes
    terminate_button = ttk.Button(
        tab,
        text="Terminate Process",
        command=lambda: on_terminate_process(tab, system_utils.terminate_process)
    )
    terminate_button.grid(row=1, column=0, padx=5, pady=5, sticky='w')

    priority_button = ttk.Button(
        tab,
        text="Change Priority",
        command=lambda: on_change_priority(tab, system_utils.set_process_priority)
    )
    priority_button.grid(row=1, column=1, padx=5, pady=5, sticky='e')

    # Store the widgets so we can interact with them later
    tab.process_listbox = process_listbox
    tab.terminate_button = terminate_button
    tab.priority_button = priority_button

    # Configure row and column weights to make the widgets expand
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)

    update_process_manager_tab(tab, system_utils.get_running_processes())

def update_process_manager_tab(tab, processes):
    """Updates the data displayed in the Process Manager tab."""
    tab.process_listbox.delete(0, tk.END)  # Clear the listbox
    for process in processes:
        tab.process_listbox.insert(
            tk.END,
            f"{process['name']} (PID: {process['pid']}, CPU: {process['cpu_percent']}%, Memory: {process['memory_percent']}%)",
        )

    tab.after(1000, update_process_manager_tab, tab, system_utils.get_running_processes())

# New functions for process management actions
def get_selected_process_pid(tab):
    """Gets the PID of the selected process in the process listbox."""
    try:
        selection = tab.process_listbox.curselection()
        print(selection)
        if selection:
            selected_item = tab.process_listbox.get(selection[0])
            print("Printing the Selected Item")
            print(selected_item)
            pid_str = selected_item.split("(PID: ")[1].split(",")[0]
            return int(pid_str)
        else:
            return None
    except IndexError:
        return None

def on_terminate_process(tab, terminate_process_func):
    """Handles the "Terminate Process" button click."""
    pid = get_selected_process_pid(tab)
    if pid:
        if messagebox.askyesno("Confirm", f"Terminate process with PID {pid}?"):
            if terminate_process_func(pid):
                messagebox.showinfo("Success", f"Process with PID {pid} terminated.")
            else:
                messagebox.showerror("Error", f"Failed to terminate process with PID {pid}.")
            processes = system_utils.get_running_processes()
            update_process_manager_tab(tab, processes)
    else:
        messagebox.showwarning("Warning", "No process selected.")

def on_change_priority(tab, set_process_priority_func):
    """Handles the "Change Priority" button click."""
    pid = get_selected_process_pid(tab)
    if pid:
        priority = simpledialog.askstring(
            "Input", "Enter new priority (high, above_normal, normal, below_normal, idle):"
        )
        if priority:
            if set_process_priority_func(pid, priority.lower()):
                messagebox.showinfo(
                    "Success", f"Priority of process with PID {pid} changed to {priority}."
                )
            else:
                messagebox.showerror(
                    "Error", f"Failed to change priority of process with PID {pid}."
                )
            processes = system_utils.get_running_processes()
            update_process_manager_tab(tab, processes)
    else:
        messagebox.showwarning("Warning", "No process selected.")


# -----------------------------------------------------------------------------
# Startup Manager Tab
# -----------------------------------------------------------------------------

def create_startup_manager_tab(tab):
    """Creates the content for the Startup Manager tab."""
    # Listbox to display startup programs
    startup_listbox = tk.Listbox(tab)
    startup_listbox.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Buttons to enable/disable startup programs
    enable_button = ttk.Button(tab, text="Enable", command=lambda: on_enable_startup(tab))
    enable_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    disable_button = ttk.Button(tab, text="Disable", command=lambda: on_disable_startup(tab))
    disable_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")

    # Store the widgets
    tab.startup_listbox = startup_listbox
    tab.enable_button = enable_button
    tab.disable_button = disable_button

    # Configure row and column weights to make the widgets expand
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)

    # Initial update
    update_startup_manager_tab(tab, system_utils.get_startup_programs())

def update_startup_manager_tab(tab, startup_programs):
    """Updates the data displayed in the Startup Manager tab."""
    tab.startup_listbox.delete(0, tk.END)
    for program in startup_programs:
        tab.startup_listbox.insert(tk.END, program)

def on_enable_startup(tab):
    selected = tab.startup_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No program selected.")
        return
    
    item = tab.startup_listbox.get(selected[0])
    name = item.split(":")[0].strip()

    result = messagebox.askyesno(
        "Confirm Enable",
        f"Do you want to enable '{name}' at startup?"
    )
    if result:
        # Example path — in a real app, store full path in list or use file dialog
        success = system_utils.enable_startup_program(name, f"C:\\Path\\To\\{name}.exe")
        if success:
            messagebox.showinfo("Success", f"'{name}' enabled at startup.")
            update_startup_manager_tab(tab, system_utils.get_startup_programs())
        else:
            messagebox.showerror("Error", f"Failed to enable '{name}'.")


def on_disable_startup(tab):
    selected = tab.startup_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No program selected.")
        return
    
    item = tab.startup_listbox.get(selected[0])
    name = item.split(":")[0].strip()

    result = messagebox.askyesno(
        "Confirm Disable",
        f"Do you want to disable '{name}' from starting automatically?"
    )
    if result:
        success = system_utils.disable_startup_program(name)
        if success:
            messagebox.showinfo("Success", f"'{name}' disabled from startup.")
            update_startup_manager_tab(tab, system_utils.get_startup_programs())
        else:
            messagebox.showerror("Error", f"Failed to disable '{name}'.")

# -----------------------------------------------------------------------------
# AI Assitance Tab
# -----------------------------------------------------------------------------

def create_ai_assistance_tab(tab, ai_client):
    """Creates the content for the AI Assistance tab (Single Text Area)."""
    # Text area to display the entire chat history
    chat_display = tk.Text(tab)
    chat_display.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    chat_display.config(state=tk.DISABLED)  # Make it read-only for display

    # Entry field for user input
    user_input_entry = ttk.Entry(tab)
    user_input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")  # Span across column 0

    # Button to send the query to the AI
    send_button = ttk.Button(
        tab, text="Send", command=lambda: _send_user_input(tab, ai_client, chat_display)
    )
    send_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")  # In row 2, column 0

    # Button to clear chat history
    clear_history_button = ttk.Button(
        tab, text="Clear History", command=lambda: _clear_chat_history(tab, ai_client, chat_display)
    )
    clear_history_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")  # In row 2, column 1

    # Store the widgets and the ai_client
    tab.chat_display = chat_display
    tab.user_input_entry = user_input_entry
    tab.send_button = send_button
    tab.clear_history_button = clear_history_button
    tab.ai_client = ai_client

    # Configure row and column weights to make the widgets expand
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_rowconfigure(1, weight=0)
    tab.grid_rowconfigure(2, weight=0)
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)

def _send_user_input(tab, ai_client, chat_display):
    """Handles sending user input to the AI and displaying the response (Single Text Area)."""
    user_input = tab.user_input_entry.get()
    tab.user_input_entry.delete(0, tk.END)

    _display_chat_message(chat_display, f"User: {user_input}\n")

    def get_ai_response():
        """Gets the AI response in a separate thread (Single Text Area)."""
        try:
            ai_response = ai_client.get_response(user_input)
            tab.after(0, _display_ai_response_single, tab, ai_response, chat_display)
        except Exception as e:
            tab.after(0, _display_ai_response_single, tab, f"Error: {e}", chat_display)

    thread = threading.Thread(target=get_ai_response)
    thread.start()

def _display_ai_response_single(tab, response, chat_display):
    """Displays the AI's response in the single chat display (Single Text Area)."""
    _display_chat_message(chat_display, f"SysSKY: {response}\n")

def _display_chat_message(chat_display, message):
    """Helper function to display a message in the chat display."""
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, message)
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def _clear_chat_history(tab, ai_client, chat_display):
    """Clears the chat history (Single Text Area)."""
    ai_client.reset_chat()
    chat_display.config(state=tk.NORMAL)
    chat_display.delete("1.0", tk.END)
    chat_display.config(state=tk.DISABLED)



