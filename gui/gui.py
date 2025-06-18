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
        },
        # Added Treeview styling for dark theme
        "Treeview": {
            "configure": {
                "background": accent_color,
                "foreground": fg_color,
                "fieldbackground": accent_color,
                "font": normal_font
            },
            "map": {
                "background": [("selected", highlight_color)],
                "foreground": [("selected", bg_color)]
            }
        },
        "Treeview.Heading": {
            "configure": {
                "background": button_bg,
                "foreground": fg_color,
                "font": header_font
            },
            "map": {
                "background": [("active", highlight_color)],
                "foreground": [("active", bg_color)]
            }
        },
        # Added Scrollbar styling
        "Vertical.TScrollbar": {
            "configure": {
                "background": button_bg,
                "troughcolor": accent_color,
                "bordercolor": accent_color,
                "arrowcolor": fg_color,
                "darkcolor": button_bg,
                "lightcolor": button_bg
            },
            "map": {
                "background": [("active", highlight_color)]
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
    """Creates the redesigned System Monitor tab with bar charts."""
    # Canvas dimensions
    canvas_width = 200
    canvas_height = 100

    # CPU Chart
    cpu_canvas = tk.Canvas(tab, width=canvas_width, height=canvas_height, bg="#3A506B", highlightthickness=0)
    cpu_canvas.grid(row=0, column=0, padx=10, pady=10)
    cpu_label = ttk.Label(tab, text="CPU", anchor="center")
    cpu_label.grid(row=1, column=0)

    # RAM Chart
    ram_canvas = tk.Canvas(tab, width=canvas_width, height=canvas_height, bg="#3A506B", highlightthickness=0)
    ram_canvas.grid(row=0, column=1, padx=10, pady=10)
    ram_label = ttk.Label(tab, text="RAM", anchor="center")
    ram_label.grid(row=1, column=1)

    # Disk Chart (we'll show total used % across all partitions for simplicity)
    disk_canvas = tk.Canvas(tab, width=canvas_width, height=canvas_height, bg="#3A506B", highlightthickness=0)
    disk_canvas.grid(row=0, column=2, padx=10, pady=10)
    disk_label = ttk.Label(tab, text="Disk", anchor="center")
    disk_label.grid(row=1, column=2)

    # Save for updates
    tab.cpu_canvas = cpu_canvas
    tab.ram_canvas = ram_canvas
    tab.disk_canvas = disk_canvas

    update_system_monitor_tab(tab)

def update_system_monitor_tab(tab):
    """Updates the system monitor tab with live chart data."""
    cpu = system_utils.get_cpu_usage()
    ram_total, ram_used = system_utils.get_ram_usage()
    disk_info = system_utils.get_disk_usage()

    ram_percent = (ram_used / ram_total) * 100 if ram_total > 0 else 0
    total_disk = sum(d['total'] for d in disk_info if not d.get("error"))
    used_disk = sum(d['used'] for d in disk_info if not d.get("error"))
    disk_percent = (used_disk / total_disk) * 100 if total_disk > 0 else 0

    draw_usage_bar(tab.cpu_canvas, cpu, "CPU")
    draw_usage_bar(tab.ram_canvas, ram_percent, "RAM")
    draw_usage_bar(tab.disk_canvas, disk_percent, "Disk")

    tab.after(1000, update_system_monitor_tab, tab)

def draw_usage_bar(canvas, percent, label):
    """Draws a usage bar inside a canvas based on percentage."""
    canvas.delete("all")
    width = int(canvas.winfo_width())
    height = int(canvas.winfo_height())
    fill_width = int((percent / 100) * width)

    # Background bar
    canvas.create_rectangle(0, 0, width, height, fill="#2C3E50", outline="")

    # Foreground bar
    canvas.create_rectangle(0, 0, fill_width, height, fill="#5BC0BE", outline="")

    # Text in the center
    canvas.create_text(width // 2, height // 2, text=f"{percent:.1f}%", fill="#E0E0E0", font=("Arial", 14, "bold"))


# -----------------------------------------------------------------------------
# Process Manager Tab
# -----------------------------------------------------------------------------

def create_process_manager_tab(tab):
    """Creates the content for the Process Manager tab using Treeview."""
    # Treeview to display processes
    process_tree = ttk.Treeview(tab, columns=("PID", "Name", "CPU", "Memory"), show="headings", selectmode="browse")
    process_tree.heading("PID", text="PID")
    process_tree.heading("Name", text="Process Name")
    process_tree.heading("CPU", text="CPU %")
    process_tree.heading("Memory", text="Memory %")
    process_tree.column("PID", width=80, anchor=tk.W)
    process_tree.column("Name", width=250, anchor=tk.W)
    process_tree.column("CPU", width=80, anchor=tk.CENTER)
    process_tree.column("Memory", width=100, anchor=tk.CENTER)
    process_tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    # Scrollbar
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=process_tree.yview)
    process_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=3, sticky="ns", pady=5)

    # Buttons
    terminate_button = ttk.Button(tab, text="Terminate Process", command=lambda: on_terminate_process(tab, system_utils.terminate_process))
    terminate_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    priority_button = ttk.Button(tab, text="Change Priority", command=lambda: on_change_priority(tab, system_utils.set_process_priority))
    priority_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")

    # Store references
    tab.process_tree = process_tree
    tab.terminate_button = terminate_button
    tab.priority_button = priority_button
    tab.selected_pid = None
    tab.pid_map = {}

    # Events and layout
    process_tree.bind("<<TreeviewSelect>>", lambda e: on_process_select(e, tab))
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)

    # Initial update
    update_process_manager_tab(tab, system_utils.get_running_processes())

def update_process_manager_tab(tab, processes):
    """Updates the Treeview in the Process Manager tab, preserving selection."""
    previously_selected_pid = tab.selected_pid
    tree = tab.process_tree
    tree.delete(*tree.get_children())  # Clear current entries
    tab.pid_map = {}

    for process in processes:
        pid = process["pid"]
        name = process["name"]
        cpu = f"{process['cpu_percent']:.1f}"
        mem = f"{process['memory_percent']:.1f}"
        item_id = tree.insert("", tk.END, values=(pid, name, cpu, mem))
        tab.pid_map[item_id] = pid

    # Restore selection
    if previously_selected_pid:
        for item_id, pid in tab.pid_map.items():
            if pid == previously_selected_pid:
                tree.selection_set(item_id)
                tree.see(item_id)
                break
        else:
            tab.selected_pid = None

    tab.after(1000, update_process_manager_tab, tab, system_utils.get_running_processes())

def on_process_select(event, tab):
    """Triggered when a user selects a process in the Treeview."""
    selected = tab.process_tree.selection()
    if selected:
        item_id = selected[0]
        pid = tab.pid_map.get(item_id)
        tab.selected_pid = pid
    else:
        tab.selected_pid = None

def get_selected_process_pid(tab):
    """Returns the PID of the selected process, if any."""
    return tab.selected_pid

def on_terminate_process(tab, terminate_process_func):
    """Terminate the selected process."""
    pid = get_selected_process_pid(tab)
    if pid:
        if messagebox.askyesno("Confirm", f"Terminate process with PID {pid}?"):
            if terminate_process_func(pid):
                messagebox.showinfo("Success", f"Process with PID {pid} terminated.")
                tab.selected_pid = None
            else:
                messagebox.showerror("Error", f"Failed to terminate process with PID {pid}.")
    else:
        messagebox.showwarning("Warning", "No process selected.")

def on_change_priority(tab, set_process_priority_func):
    """Change the priority of the selected process."""
    pid = get_selected_process_pid(tab)
    if pid:
        priority = simpledialog.askstring(
            "Input", "Enter new priority (high, above_normal, normal, below_normal, idle):"
        )
        if priority:
            if set_process_priority_func(pid, priority.lower()):
                messagebox.showinfo("Success", f"Priority of PID {pid} changed to {priority}.")
            else:
                messagebox.showerror("Error", f"Failed to change priority for PID {pid}.")
    else:
        messagebox.showwarning("Warning", "No process selected.")


# -----------------------------------------------------------------------------
# Startup Manager Tab - FIXED VERSION
# -----------------------------------------------------------------------------

def create_startup_manager_tab(tab):
    """Creates the content for the Startup Manager tab with Treeview."""
    # Treeview to display startup programs in a table
    startup_tree = ttk.Treeview(tab, columns=("Name", "Path"), show="headings", selectmode="browse")
    startup_tree.heading("Name", text="Program Name")
    startup_tree.heading("Path", text="Executable Path")
    startup_tree.column("Name", width=200, anchor=tk.W, minwidth=150)
    startup_tree.column("Path", width=400, anchor=tk.W, minwidth=300)
    startup_tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    # Scrollbar for the treeview
    scrollbar = ttk.Scrollbar(tab, orient="vertical", command=startup_tree.yview)
    startup_tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=3, sticky="ns", pady=5)

    # Status label to show current selection
    status_label = ttk.Label(tab, text="Select a program to enable/disable")
    status_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    # Buttons to enable/disable startup programs
    enable_button = ttk.Button(tab, text="Enable", 
                              command=lambda: on_enable_startup(tab))
    enable_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    disable_button = ttk.Button(tab, text="Disable", 
                               command=lambda: on_disable_startup(tab))
    disable_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    # Store references to widgets in the tab
    tab.startup_tree = startup_tree
    tab.status_label = status_label
    tab.enable_button = enable_button
    tab.disable_button = disable_button
    tab.selected_program_name = None
    tab.selected_program_path = None

    # Configure tab grid weights
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)

    # Bind selection event
    startup_tree.bind("<<TreeviewSelect>>", lambda e: on_startup_select(e, tab))

    # Initial update
    update_startup_manager_tab(tab, system_utils.get_startup_programs())



def update_startup_manager_tab(tab, startup_programs):
    """Updates the data displayed in the Startup Manager tab using Treeview."""
    # Clear existing items
    for item in tab.startup_tree.get_children():
        tab.startup_tree.delete(item)
    
    # Clear selection tracking
    tab.selected_program_name = None
    tab.selected_program_path = None

    if not startup_programs:
        # Insert a placeholder item when no programs are found
        tab.startup_tree.insert("", tk.END, values=("No startup programs found", ""), tags=("placeholder",))
        tab.startup_tree.tag_configure("placeholder", foreground="gray")
        return

    for program in startup_programs:
        try:
            # Handle the program string format "name: path"
            if ":" in program:
                name, path = program.split(":", 1)  # Split only on first colon
                name = name.strip()
                path = path.strip()
            else:
                # Handle cases where there's no colon separator
                name = program.strip()
                path = "Path not available"
            
            # Insert the program into the treeview
            tab.startup_tree.insert("", tk.END, values=(name, path))
            
        except Exception as e:
            # Handle any parsing errors gracefully
            tab.startup_tree.insert("", tk.END, values=("Error parsing entry", str(program)))

def on_startup_select(event, tab):
    """Callback function when a startup program is selected."""
    selected_items = tab.startup_tree.selection()
    if selected_items:
        item = selected_items[0]
        values = tab.startup_tree.item(item, "values")
        
        if len(values) >= 2 and values[0] != "No startup programs found":
            tab.selected_program_name = values[0]
            tab.selected_program_path = values[1]
            tab.status_label.config(text=f"Selected: {tab.selected_program_name}")
        else:
            tab.selected_program_name = None
            tab.selected_program_path = None
            tab.status_label.config(text="Invalid selection")
    else:
        tab.selected_program_name = None
        tab.selected_program_path = None
        tab.status_label.config(text="No program selected")







def on_enable_startup(tab):
    """Handles enabling a selected startup program."""
    if not tab.selected_program_name or tab.selected_program_name == "No startup programs found":
        messagebox.showwarning("Warning", "Please select a program to enable.")
        return
    
    # For programs that might be disabled, we need to re-enable them
    # This assumes the program path is available
    if not tab.selected_program_path or tab.selected_program_path == "Path not available":
        # Ask user for the path if not available
        path = simpledialog.askstring(
            "Enable Startup Program",
            f"Enter the full executable path for '{tab.selected_program_name}':\n(e.g., C:\\Program Files\\MyApp\\MyApp.exe)"
        )
        if not path:
            return
    else:
        path = tab.selected_program_path
    
    # Confirm the action
    confirm_message = f"Enable '{tab.selected_program_name}' at startup?"
    if messagebox.askyesno("Confirm Enable", confirm_message):
        try:
            success = system_utils.enable_startup_program(tab.selected_program_name, path)
            if success:
                messagebox.showinfo("Success", f"'{tab.selected_program_name}' has been enabled at startup.")
                # Refresh the list to show updated status
                update_startup_manager_tab(tab, system_utils.get_startup_programs())
            else:
                messagebox.showerror("Error", f"Failed to enable '{tab.selected_program_name}' at startup.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def on_disable_startup(tab):
    """Handles disabling a selected startup program."""
    if not tab.selected_program_name or tab.selected_program_name == "No startup programs found":
        messagebox.showwarning("Warning", "Please select a program to disable.")
        return
    
    # Confirm the action
    confirm_message = f"Disable '{tab.selected_program_name}' from starting automatically?"
    if messagebox.askyesno("Confirm Disable", confirm_message):
        try:
            success = system_utils.disable_startup_program(tab.selected_program_name)
            if success:
                messagebox.showinfo("Success", f"'{tab.selected_program_name}' has been disabled from startup.")
                # Refresh the list to show updated status
                update_startup_manager_tab(tab, system_utils.get_startup_programs())
            else:
                messagebox.showerror("Error", f"Failed to disable '{tab.selected_program_name}' from startup.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

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
