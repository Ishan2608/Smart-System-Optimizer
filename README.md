# 🧠 Smart System Optimizer

A full-featured, intelligent system monitoring and management tool written in Python. It combines real-time performance tracking, advanced process control, robust startup program configuration, and conversational AI support — all within a clean, responsive graphical user interface using `tkinter`.

This project mimics and enhances the core functionality of Windows Task Manager, providing users with deeper insights, more control, and educational assistance for optimizing their system's performance.

## 📁 Project Structure Overview

The project follows a modular structure to ensure maintainability and clear separation of concerns.

SmartSystemOptimizer/├── main.py                     # Application entry point and main loop.├── core/│   ├── init.py             # Python package initializer for 'core'.│   ├── ai_client.py            # Handles integration with the Google Gemini AI API.│   └── system_utils.py         # Contains OS-level logic for system monitoring, process management, and startup control.└── gui/├── init.py             # Python package initializer for 'gui'.├── gui.py                  # Defines the main GUI layout, tab structures, and widget interactions.└── helpers.py              # Provides common UI helper functions (e.g., message dialogs).
## 🎛️ Features and Functional Tabs

The application is organized into four distinct tabs, each serving a specific purpose in system optimization.

### 🔹 1. System Monitor Tab

This tab provides real-time visual and numerical data on key system resources.

* **Continuous Display:** Continuously monitors and displays **CPU**, **RAM**, and **Disk** usage.

* **Visual Charts:** Uses `tk.Canvas` to draw dynamic bar charts whose fill width directly corresponds to the usage percentage, offering an intuitive visual overview.

* **Numerical Labels:** Accompanying `ttk.Label` widgets dynamically update text (e.g., "CPU: 47%", "RAM: Used X GB / Total Y GB").

* **Update Interval:** Values update every second using Tkinter's non-blocking `.after(1000, update_function)`.

**Backend Methods Used (`core/system_utils.py`):**

* `get_cpu_usage(interval=0.1)`: Returns the current CPU usage as a percentage via `psutil.cpu_percent()`. The interval is for internal `psutil` calculation.

* `get_ram_usage()`: Returns a tuple of total and used RAM in GB using `psutil.virtual_memory()`.

* `get_disk_usage()`: Iterates through system disk partitions via `psutil.disk_partitions()` and `psutil.disk_usage()`, returning total and used space for each in GB. Includes error handling for `PermissionError`.

**Logic Highlights:**

* **Responsive Updates:** Metrics are refreshed directly within the Tkinter event loop using `after()` to ensure the GUI remains responsive.

* **Aggregated Disk View:** For the chart, disk usage aggregates total and used space across all accessible partitions to provide a holistic view.

* **Error Handling:** Disk usage gracefully handles `PermissionError` for inaccessible partitions.

### 🔹 2. Process Manager Tab

This tab provides comprehensive control over running processes on the system.

* **Tabular Listing:** Lists **all active processes** in a `ttk.Treeview` widget, offering a structured, sortable table format.

    * **Columns:** Displays "PID", "Process Name", "CPU %", and "Memory %".

* **Persistent Selection:** A crucial feature: when processes update (every 1 second), the user's selected process remains highlighted and selected, preventing accidental loss of selection due to list refreshing. This is achieved by using the process's PID as the `Treeview` item ID (`iid`) and re-selecting it if it's still present.

* **Color Coding:** Processes with high CPU usage (e.g., >50%) or memory usage (e.g., >50%) are highlighted in red to quickly draw attention to resource-intensive applications.

* **Actions:**

    * **Terminate Process:** Allows the user to gracefully terminate a selected process.

    * **Change Priority:** Prompts the user to set a new priority level (e.g., "high", "normal", "idle") for the selected process.

**Backend Methods Used (`core/system_utils.py`):**

* `get_running_processes()`: Uses `psutil.process_iter()` to efficiently gather essential details (PID, name, CPU usage, memory usage) for all running processes. Includes robust error handling for `psutil.NoSuchProcess`, `psutil.AccessDenied`, and `psutil.ZombieProcess`.

* `terminate_process(pid)`: Attempts to terminate the process identified by its PID using `psutil.Process(pid).terminate()` and `proc.wait()`. Returns `True` on success, `False` on failure (e.g., `NoSuchProcess`, `AccessDenied`).

* `set_process_priority(pid, level)`: Sets the priority of the given process.

    * **Windows:** Maps priority levels to `psutil` constants like `psutil.HIGH_PRIORITY_CLASS`, `psutil.NORMAL_PRIORITY_CLASS`, etc.

    * **Unix (Linux/macOS):** Uses `proc.nice()` with standard nice values (e.g., `-10` for high, `19` for idle). Handles `NoSuchProcess` and `AccessDenied` exceptions.

**Logic Highlights:**

* **PID as `iid`:** The unique Process ID (PID) is used as the internal item identifier (`iid`) for `Treeview` entries. This is fundamental for maintaining selection across updates, as PIDs are stable while display indices are not.

* **Event Binding:** `process_tree.bind("<<TreeviewSelect>>", ...)` captures user selections to update the `tab.selected_pid` attribute.

* **Error Reporting:** Utilizes `messagebox.showinfo`, `messagebox.showerror`, and `messagebox.showwarning` to provide clear feedback to the user on success or failure of process operations, including potential `Access Denied` errors.

### 🔹 3. Startup Manager Tab

This tab provides detailed information and control over programs that launch automatically when the system starts (currently Windows-specific).

* **Tabular Listing:** Displays startup entries in a `ttk.Treeview` widget.

    * **Columns:** Shows "Program Name", "Executable Path", and "Status" (e.g., "enabled", "disabled").

* **Comprehensive Scanning (Windows):** Gathers startup entries from key Windows Registry locations:

    * `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`

    * `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run`

    * `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run`

    * `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run`

* **Path Caching:** Implements an in-memory `disabled_program_cache` to store paths of programs that were disabled by the application. This allows `enable_startup_program` to restore the correct path even if the program was removed from the "Run" key.

* **Actions:**

    * **Enable:** Adds or re-enables a selected program to the startup registry. Requires the full executable path (can be entered by the user).

    * **Disable:** Removes a program from the active startup registry entries and marks it as "disabled" in `StartupApproved`.

    * **Restore Path:** Allows the user to manually provide a path for a disabled or orphaned startup entry, effectively re-enabling it with the correct executable path.

* **Status Indicators:** `Treeview` rows for disabled programs are visually differentiated (e.g., text color is greyed out) using `tag_configure()`.

* **Platform Awareness:** Clearly indicates if startup management is not supported on the current operating system (e.g., non-Windows).

**Backend Methods Used (`core/system_utils.py`):**

* `get_startup_programs()`: Orchestrates reading from various registry keys to compile a comprehensive list of startup programs, their paths, and their enable/disable status. Integrates the `disabled_program_cache`.

* `enable_startup_program(name, path, scope)`: Writes the program name and path to the appropriate "Run" registry key (`HKCU` or `HKLM` based on `scope`) and sets its status to `0x02` (enabled) in the `StartupApproved` key. Handles `KEY_WOW64_64KEY` for 64-bit systems.

* `disable_startup_program(name)`: Removes the program's entry from the "Run" registry key and sets its status to `0x03` (disabled) in the `StartupApproved` key. Critically, it caches the program's path before removal.

**Logic Highlights:**

* **Registry Interaction:** Directly interacts with the Windows Registry using the `winreg` module, which often requires administrative privileges for `HKLM` operations.

* **Scope Detection:** Infers `user` vs. `machine` scope for `enable` operations based on common Windows paths (`Program Files`, `ProgramData`).

* **Robust Disabling:** When a program is disabled, its original path is remembered in `disabled_program_cache` so it can be re-enabled correctly later.

* **User Input for Paths:** `simpledialog.askstring` is used to prompt the user for executable paths when enabling a new program or restoring a missing path.

### 🔹 4. AI Assistant Tab

This tab provides an interactive chatbot interface powered by the Google Gemini API, offering AI-driven insights and assistance.

* **Conversational Interface:** Features a `tk.Text` widget for displaying chat history and a `ttk.Entry` for user input.

* **Background Processing:** AI responses are fetched in a separate `threading.Thread` to prevent the GUI from freezing during network requests.

* **Chat History Management:**

    * `Send` button: Sends the user's query to the AI, displays it in the chat, and then appends the AI's response.

    * `Clear History` button: Clears the displayed chat history and resets the AI model's internal chat context, ensuring fresh conversations.

* **System Context:** The AI is initialized with a "system profile" containing details like OS version, CPU, RAM, disk, and network information, allowing it to provide more relevant and contextual advice.

**Backend (`core/ai_client.py`) Methods Used:**

* `AIClient.__init__(api_key, model_name)`: Initializes the `google.generativeai.Client` and creates a chat session. Also gathers initial `_get_system_profile()`.

* `_initialize_chat_with_role()`: Sends a system prompt to the AI to define its persona ("SysSKY, an AI assistant developed by Team SysSKY") and its purpose (to help users with system understanding and optimization).

* `_get_system_profile()`: Collects detailed system information (OS, CPU counts, RAM, swap, detailed disk info, network interface addresses) using `platform` and `psutil`. This profile is included in prompts sent to the AI.

* `get_response(prompt)`: Takes a user prompt, augments it with the system profile, and sends it to the Gemini API. Returns the AI's textual response. Includes `try-except` for API call errors.

* `reset_chat()`: Clears the `self.chat` object's history, effectively starting a new conversation with the AI.

* `get_chat_history_for_display()`: Formats the AI chat history into a string suitable for display in the Tkinter `Text` widget.

**Logic Highlights:**

* **Asynchronous AI Calls:** Uses `threading` to keep the GUI responsive while waiting for AI responses, then uses `after(0, ...)` to update the GUI safely from the main thread.

* **Contextual AI:** The AI receives a snapshot of the system's current state with each query, enabling it to provide relevant and personalized advice.

* **Error Resilience:** Includes error handling for API interactions.

## 🧰 Detailed Widget Overview

| **Widget** | **Module** | **Used In** | **Purpose** |
|---|---|---|---|
| `tk.Tk` | `tkinter` | `main.py`, `gui.py` | The main application window. |
| `ttk.Notebook` | `tkinter.ttk` | `gui.py` | Creates the tabbed interface for navigation between modules. |
| `ttk.Frame` | `tkinter.ttk` | `gui.py` | Container for widgets within each tab. |
| `ttk.Label` | `tkinter.ttk` | All tabs | Displays static text labels and dynamic system usage values. |
| `tk.Canvas` | `tkinter` | System Monitor | Draws dynamic bar charts for CPU, RAM, and Disk usage. |
| `ttk.Treeview` | `tkinter.ttk` | Process Manager, Startup Manager | Displays tabular data with multiple columns and supports selection. |
| `ttk.Button` | `tkinter.ttk` | All tabs | Triggers actions (e.g., Terminate, Change Priority, Send, Clear). |
| `ttk.Entry` | `tkinter.ttk` | AI Assistant | Allows single-line text input (e.g., user queries). |
| `tk.Text` | `tkinter` | AI Assistant, System Monitor (Disk) | Displays multi-line text (chat history, detailed disk info). |
| `ttk.Scrollbar` | `tkinter.ttk` | Process Manager, Startup Manager, AI Assistant | Provides scrolling functionality for `Treeview` and `Text` widgets. |
| `simpledialog` | `tkinter.simpledialog` | Process Manager, Startup Manager | Provides simple popup dialogs for text input (e.g., new priority, path). |
| `messagebox` | `tkinter.messagebox` | All modules (`main.py`, `gui.py`, `system_utils.py`) | Displays informational, warning, and error messages to the user. |

## 🔁 Program Flow

The application initializes and operates through a well-defined flow:

1.  **Application Start (`main.py`):**

    * The `main()` function is the application's entry point.

    * It attempts to get the AI API key (e.g., from an environment variable).

    * It instantiates the `AIClient` from `core/ai_client.py`.

    * It creates the main Tkinter window (`root`).

    * It then calls `gui.create_tabs(root, ai_client_instance)` to set up the entire tabbed GUI.

    * Finally, `root.mainloop()` is called to start the Tkinter event loop, making the GUI interactive.

    * A `try-except` block handles general initialization errors, displaying a message box and cleaning up if the window was created.

2.  **GUI Creation (`gui.py`):**

    * `create_main_window()` sets up the main `tk.Tk()` instance, its title, geometry, and applies the custom dark theme.

    * `create_tabs()` creates the `ttk.Notebook` (tab container) and individual `ttk.Frame` instances for each tab (System Monitor, Process Manager, Startup Manager, AI Assistance). It also calls specific `create_..._tab()` functions for each, passing the respective tab frame and the `ai_client_instance`.

3.  **Tab Initialization (`gui.py`):**

    * Each `create_..._tab()` function (`create_system_monitor_tab`, `create_process_manager_tab`, etc.) is responsible for laying out the widgets specific to its tab (e.g., labels, canvases, treeviews, buttons).

    * They also initiate the first data fetch and schedule recurring updates using `tab.after()`.

4.  **Real-time Updates (`gui.py` & `core/system_utils.py`):**

    * Functions like `update_system_monitor_tab` and `update_process_manager_tab` are called repeatedly (e.g., every 1000ms) by `tab.after()`.

    * These update functions call into `core/system_utils.py` to fetch fresh system data (CPU, RAM, Disk, Processes).

    * The fetched data is then used to update the respective GUI widgets.

    * For the Process Manager, the `Treeview` is refreshed, but user selection is preserved using the PID as the `iid` and `tree.see()` to keep the selected item in view.

5.  **User Interactions:**

    * **Button Clicks:** `ttk.Button` widgets are configured with `command` attributes that trigger specific functions (`on_terminate_process`, `on_change_priority`, `_send_user_input`, etc.) when clicked.

    * **Treeview Selection:** `<<TreeviewSelect>>` events are bound to `on_process_select` and `on_startup_select` to capture the currently selected item's data (e.g., PID for processes, Name/Path/Status for startup programs).

    * **Dialogs:** `tkinter.messagebox` and `tkinter.simpledialog` are used for user confirmations, input, and error reporting.

6.  **Backend Operations (`core/system_utils.py`):**

    * Functions in `system_utils.py` directly interact with the operating system using `psutil` for performance metrics and process control, and `winreg` (on Windows) for startup program management.

    * Error handling (`try-except`) is employed at the backend level to catch `psutil` specific errors (e.g., `NoSuchProcess`, `AccessDenied`) and `winreg` related `OSError` or other exceptions, providing a safe wrapper for system calls.

7.  **AI Interaction (`core/ai_client.py`):**

    * User input from the AI Assistance tab is passed to `ai_client.get_response()`.

    * This method augments the prompt with the system profile and sends it to the Gemini API.

    * AI responses are then displayed back in the chat history, ensuring the GUI remains responsive by running the API call in a separate thread.

    * Chat history can be cleared via `ai_client.reset_chat()`.

## 💎 Visual Design and Theme

The application features a consistent dark-themed interface designed for clarity and ease of use:

* **Primary Background:** `#1E2430` (dark blue-gray)

* **Foreground (Labels/Text):** `#E0E0E0` (light gray)

* **Accent Color:** `#3A506B` (a slightly lighter dark blue-gray, used for subtle backgrounds in inputs/treeview)

* **Highlight/Accent Color:** `#5BC0BE` (teal, used for active states, selected tabs, button hover, and progress bar fills)

* **Button Background:** `#2C3E50` (darker blue-gray)

* **Treeview Styling:**

    * Dark background with light foreground.

    * Custom heading styles for better visibility.

    * `tag_configure()` is used for visual cues, such as greyed-out text for disabled startup programs or red text for high-usage processes.

* **Theme Application:** The theme is applied primarily using `ttk.Style()` for `ttk` widgets and direct `configure()` calls for standard `tk` widgets, ensuring a unified look. A recursive `configure_widgets` helper function applies styles to all child widgets.

## ✅ Final Capabilities Checklist

| **Feature** | **Status** |
|---|---|
| Live system resource display (CPU, RAM, Disk) | ✅ |
| Visual bar charts for system resource usage | ✅ |
| Display and control over running processes in a tabular `Treeview` | ✅ |
| Persistent selection of processes across updates | ✅ |
| Ability to terminate any selected process | ✅ |
| Ability to adjust priorities of any selected process (Windows & Unix) | ✅ |
| View all Windows startup entries (name, path, status) | ✅ |
| Ability to enable/disable Windows startup programs | ✅ |
| Ability to restore missing paths for disabled startup programs | ✅ |
| Intelligent AI support using the Google Gemini API with system context | ✅ |
| Error-safe: all backend calls are guarded with `try/except` | ✅ |
| Self-contained: no external GUI frameworks needed beyond standard Python libraries. | ✅ |
| User-friendly dark-themed GUI | ✅ |

## 🚀 Setup and Running

To set up and run the Smart System Optimizer, follow these steps:

1.  **Clone the Repository:**

    ```bash
    git clone <Your-GitHub-Repo-URL>
    cd SmartSystemOptimizer


    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate


    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt


    ```

    (Ensure `requirements.txt` contains `psutil` and `google-generativeai`).

4.  **Set up Gemini API Key:**

    * Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

    * Set it as an environment variable named `GEMINI_API_KEY` (or `AI_CLIENT` as used in `main.py`).

        * **Windows (Command Prompt):**

            ```bash
            set AI_CLIENT=YOUR_GEMINI_API_KEY


            ```

        * **Windows (PowerShell):**

            ```powershell
            $env:AI_CLIENT="YOUR_GEMINI_API_KEY"


            ```

        * **macOS/Linux:**

            ```bash
            export AI_CLIENT=YOUR_GEMINI_API_KEY


            ```

        * **Alternatively, you can load it from a `.env` file** using `python-dotenv`. If you choose this, make sure `load_dotenv()` is uncommented in `main.py` and `ai_client.py` and `python-dotenv` is in your `requirements.txt`.

5.  **Run the Application:**

    ```bash
    python main.py


    ```

## 📦 Dependencies

* **`psutil`**: Cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network).

* **`tkinter`**: Python's standard GUI (Graphical User Interface) toolkit.

* **`google-generativeai`**: Python client library for the Google Gemini API.

* (Optional but recommended: `python-dotenv` for local environment variable management).

## 🛠️ Troubleshooting

* **"Missing positional argument" / API Key Errors:**

    * Ensure your `GEMINI_API_KEY` (or `AI_CLIENT`) environment variable is correctly set *before* running `main.py`.

    * Verify that `from core import GEMINI_API_KEY, GEMINI_MODEL_NAME` (or similar) in `ai_client.py` correctly points to where your API key is defined/accessed.

* **`winreg` Module Not Found / Startup Tab Issues (Non-Windows):**

    * The `winreg` module is exclusive to Windows. The Startup Manager tab's functionality will not work on macOS or Linux and will display a message indicating this.

* **"Access Denied" Errors (Process/Startup Manager):**

    * Many system-level operations (e.g., terminating critical processes, changing priority of system processes, modifying `HKEY_LOCAL_MACHINE` registry keys) require **administrative privileges**.

    * **On Windows:** Run your terminal or command prompt "As Administrator" before launching `main.py`.

* **"PID 0.0" / Empty Memory / No Selection in Process Manager:**

    * This indicates a problem where `psutil` might not be able to retrieve proper PID or memory values, or there's an issue in `gui.py`'s `Treeview` population.

    * **Check `system_utils.py`:** Ensure `proc.info['pid']` and `proc.info['memory_percent']` are reliably returning data. Adding `print()` statements in `get_running_processes()` can help diagnose what `psutil` is returning.

    * **Permissions:** Again, confirm the application has necessary permissions.

* **GUI Freezing:**

    * Most long-running operations (like AI API calls) are already threaded. Ensure any *new* intensive tasks are also moved to background threads to prevent the Tkinter GUI from becoming unresponsive.
