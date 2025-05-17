# Smart System Optimizer
A Python-based system monitoring and optimization application with AI assistance capabilities. <br>
To understand the styling code, refer to these documentations:
- [Theme_Explanation](./docs/Theme_Tutor.md)
- [Visual_Theme_Explanation](./docs/Theme_Visual_Understanding.md)

To go through a comprehensive list of QnA that provides a good overview of the concepts of operating system related to this project, refer to this document: [QnA](./docs/QnA.md)

## Project Structure
```
Smart System Optimizer/
├── main.py              # Application entry point
├── core/
│   ├── __init__.py      # Package initialization
│   ├── ai_utils.py      # AI Client integration
│   └── system_utils.py  # System monitoring utilities
└── gui/
    ├── __init__.py      # Package initialization
    ├── gui.py           # GUI elements and interactions
    └── helpers.py       # Helper functions for GUI
```

## 1. Frontend Components (GUI)

### Window and Tab Creation
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `create_main_window()` | Creates the main application window with dark theme | None | `tk.Tk` instance |
| `create_tabs(master)` | Creates the tabbed interface | `master`: Main window | Tuple of tab frames |

### System Monitor Tab
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `create_system_monitor_tab(tab)` | Creates UI for system stats display | `tab`: Frame to use | None |
| `update_system_monitor_tab(tab, cpu_usage, ram_usage, disk_usage)` | Updates displayed stats | `tab`: Tab to update, `cpu_usage`: CPU percentage, `ram_usage`: RAM stats tuple, `disk_usage`: Disk info list | None |

### Process Manager Tab
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `create_process_manager_tab(tab)` | Creates process management interface | `tab`: Frame to use | None |
| `update_process_manager_tab(tab, processes)` | Updates process listbox | `tab`: Tab to update, `processes`: List of process dictionaries | None |
| `get_selected_process_pid(tab)` | Gets PID of selected process | `tab`: Process manager tab | Integer PID or None |
| `on_terminate_process(tab, terminate_process_func)` | Handles process termination | `tab`: Process tab, `terminate_process_func`: Function reference | None |
| `on_change_priority(tab, set_process_priority_func)` | Handles priority changes | `tab`: Process tab, `set_process_priority_func`: Function reference | None |

### Startup Manager Tab
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `create_startup_manager_tab(tab)` | Creates startup program interface | `tab`: Frame to use | None |
| `update_startup_manager_tab(tab, startup_programs)` | Updates startup program list | `tab`: Tab to update, `startup_programs`: List of programs | None |

### AI Assistance Tab
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `create_ai_assistance_tab(tab, ai_client)` | Creates AI chat interface | `tab`: Frame to use, `ai_client`: AIClient instance | None |
| `_send_user_input(tab, ai_client, chat_display)` | Sends user input to AI | `tab`: AI tab, `ai_client`: AIClient instance, `chat_display`: Text widget | None |
| `_display_ai_response_single(tab, response, chat_display)` | Shows AI response | `tab`: AI tab, `response`: AI response text, `chat_display`: Text widget | None |
| `_display_chat_message(chat_display, message)` | Adds message to chat | `chat_display`: Text widget, `message`: Message text | None |
| `_clear_chat_history(tab, ai_client, chat_display)` | Clears chat history | `tab`: AI tab, `ai_client`: AIClient instance, `chat_display`: Text widget | None |

### Helper Functions
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `display_error_message(message)` | Shows error popup | `message`: Error text | None |
| `apply_dark_theme(root)` | Applies dark theme to app | `root`: Main window | None |

## 2. Backend Components

### System Utilities
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `get_cpu_usage(interval=0.1)` | Gets CPU usage | `interval`: Sampling interval in seconds | Float percentage |
| `get_ram_usage()` | Gets RAM statistics | None | Tuple (total_gb, used_gb) |
| `get_disk_usage()` | Gets disk usage for all partitions | None | List of dictionaries with partition info |
| `get_running_processes()` | Gets all running processes | None | List of process dictionaries |
| `terminate_process(pid)` | Terminates specified process | `pid`: Process ID to terminate | Boolean success value |
| `set_process_priority(pid, priority)` | Sets process priority | `pid`: Process ID, `priority`: Priority level string | Boolean success value |

### AI Client Functionality
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `__init__(api_key, model_name)` | Initializes AI client | `api_key`: Gemini API key, `model_name`: Gemini model name | None |
| `_get_system_profile()` | Collects system information | None | Dictionary with system info |
| `_get_detailed_disk_info()` | Gets detailed disk information | None | List of disk info dictionaries |
| `_get_detailed_network_info()` | Gets network interface information | None | Dictionary of network interfaces |
| `get_response(prompt)` | Gets AI response for prompt | `prompt`: User prompt text | Response text string |
| `reset_chat()` | Clears chat history | None | None |
| `get_chat_history_for_display()` | Gets formatted chat history | None | Formatted string |

### Main Application Flow
| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `update_system_info(tab)` | Updates system information periodically | `tab`: System monitor tab | None |
| `update_process_list(tab)` | Updates process list periodically | `tab`: Process manager tab | None |
| `main()` | Application entry point | None | None |

## 3. Core Built-in Functions and Libraries

### Tkinter/ttk Functions
- Window creation: `Tk()`, `withdraw()`
- Layout: `grid()`, `pack()`, `grid_rowconfigure()`, `grid_columnconfigure()`
- Widgets: `ttk.Notebook()`, `ttk.Frame()`, `ttk.Label()`, `ttk.Button()`, `ttk.Entry()`, `tk.Text()`, `tk.Listbox()`
- Control: `mainloop()`, `after()`, `config()`, `configure()`
- Style: `ttk.Style()`, `theme_create()`, `theme_use()`
- Dialogs: `messagebox.showerror()`, `messagebox.showinfo()`, `messagebox.showwarning()`, `messagebox.askyesno()`, `simpledialog.askstring()`

### psutil Functions
- System info: `cpu_percent()`, `virtual_memory()`, `swap_memory()`, `disk_partitions()`, `disk_usage()`, `net_if_addrs()`
- Process management: `process_iter()`, `Process()`, `terminate()`, `wait()`, `nice()`
- Constants: `HIGH_PRIORITY_CLASS`, `NORMAL_PRIORITY_CLASS`, etc.

### platform Functions
- System info: `system()`, `release()`, `version()`, `platform()`, `machine()`, `processor()`, `node()`, `python_version()`

### OS and System
- `os.getloadavg()`

### Threading
- `threading.Thread()`, `start()`

## 4. Program Execution Flow

1. **Application Initialization**
   ```
   main() -> create_main_window() -> create_tabs() -> apply_dark_theme()
   ```

2. **Tab Creation**
   ```
   main() -> create_system_monitor_tab()
           -> create_process_manager_tab()
           -> create_startup_manager_tab()
           -> create_ai_assistance_tab()
   ```

3. **Initial Data Loading**
   ```
   main() -> update_system_info() -> get_cpu_usage(), get_ram_usage(), get_disk_usage() -> update_system_monitor_tab()
           -> update_process_list() -> get_running_processes() -> update_process_manager_tab()
   ```

4. **Periodic Updates**
   ```
   update_system_info() -> tab.after(1000, update_system_info) [loop every 1 second]
   update_process_list() -> tab.after(5000, update_process_list) [loop every 5 seconds]
   ```

5. **User Interactions**

   a. **Process Management**
   ```
   Button click -> on_terminate_process() -> get_selected_process_pid() -> terminate_process() -> update_process_list()
                -> on_change_priority() -> get_selected_process_pid() -> set_process_priority() -> update_process_list()
   ```

   b. **AI Assistance**
   ```
   Button click -> _send_user_input() -> Thread() -> get_ai_response() -> _display_ai_response_single()
                -> _clear_chat_history() -> reset_chat()
   ```

6. **Error Handling**
   ```
   try/except blocks -> messagebox.showerror()
   ```

7. **Application Main Loop**
   ```
   main() -> root.mainloop()
   ```

## 5. Dark Theme Specifications

The application uses a dark blue-gray theme with these colors:
- Background: `#1E2430` (dark blue-gray)
- Foreground text: `#E0E0E0` (light gray)
- Accent background: `#3A506B` (medium blue-gray)
- Highlight color: `#5BC0BE` (teal accent)
- Button background: `#2C3E50` (slightly lighter blue-gray)

The theme is applied using a custom ttk style theme and recursive widget configuration for consistent styling throughout the application.
