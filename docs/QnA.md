# Questions and Answers for Viva

1.  **What is tkinter?**
    Tkinter is a standard Python library used for creating graphical user interfaces (GUIs). It's a wrapper around the Tcl/Tk toolkit.

2.  **What is ttk?**
    `ttk` (Themed Tkinter) is a module in Python that provides a set of themed widgets for Tkinter, making the GUIs look more modern and native to the operating system.

3.  **What is the difference between tkinter and ttk?**
    Tkinter provides the basic set of GUI widgets, while `ttk` offers themed versions of these widgets that have an improved look and feel. `ttk` aims for platform-native appearance.

4.  **How to create a window in Tkinter?**
    You create a main window using `root = tk.Tk()`.

5.  **Why use the mainloop() method?**
    The `mainloop()` method starts the Tkinter event loop. This loop listens for events (like button clicks, key presses) and processes them, keeping the GUI responsive.

6.  **What does geometry("800X600") method do?**
    The `geometry("800x600")` method sets the initial size of the main window to 800 pixels wide and 600 pixels high.

7.  **How to create a tabbed Interface window.**
    You create a tabbed interface using the `ttk.Notebook` widget. Each tab is typically a `ttk.Frame` added to the `Notebook`.

8.  **What does Notebook() class do and what do we pass it?**
    The `Notebook()` class creates a container for multiple tabs. You typically pass the parent window (the root or another frame) as the argument.

9.  **What is the use of Frame() class and why is it passed notebook?**
    The `Frame()` class creates a simple container widget. It's passed to the `Notebook` to act as the content area for each individual tab.

10. **Why call the add method on notebook object?**
    The `add()` method is used to add a tab (which is usually a `Frame`) to the `Notebook` widget, along with the text that will appear on the tab.

11. **How do you create a function in Python?**
    You create a function in Python using the `def` keyword followed by the function name, parentheses for parameters, a colon, and then the function's code block. Example: `def my_function(argument): ...`

12. **Why do we provide the tab argument to each function that works on modifying the contents of the frontend?**
    We provide the `tab` argument so that the function knows which specific tab (and the widgets within that tab) it should operate on or modify.

13. **Why are properties on tab object are set, e.g., tab.cpu\_label?**
    Setting properties on the `tab` object (which is usually a `Frame`) is a way to store references to the widgets created within that tab. This makes it easier to access and manipulate those specific widgets later in the code.

14. **What are tk.START and tk.END?**
    `tk.START` and `tk.END` are constants used with text widgets (`tk.Text`). `tk.START` refers to the beginning of the text, and `tk.END` refers to the end of the text.

15. **What does \<widget\>.config() method do?**
    The `<widget>.config()` method is used to access and modify the configuration options (properties) of a widget after it has been created.

16. **How do you access the properties of a widget?**
    You can access the current values of a widget's properties using the `config()` method with the property name as an argument (e.g., `widget.config('text')`).

17. **How do you set new values of a widget?**
    You set new values of a widget's properties using the `config()` method with the property name and the new value as keyword arguments (e.g., `widget.config(text='New Value')`).

18. **What is a widget()?**
    In the context of GUI programming with Tkinter, a widget is a pre-built GUI element like a button, label, text box, or window that users can interact with or that displays information.

19. **List commonly used widgets along with the classes used to create them?**
      * Label: `tk.Label`, `ttk.Label`
      * Button: `tk.Button`, `ttk.Button`
      * Entry (single-line text input): `tk.Entry`, `ttk.Entry`
      * Text (multi-line text display/input): `tk.Text`
      * Frame (container): `tk.Frame`, `ttk.Frame`
      * Notebook (tabbed interface): `ttk.Notebook`
      * Treeview (tabular data display): `ttk.Treeview`
      * Canvas (drawing area): `tk.Canvas`
      * Checkbutton: `tk.Checkbutton`, `ttk.Checkbutton`
      * Radiobutton: `tk.Radiobutton`, `ttk.Radiobutton`

20. **Why do we pass the frame, or root window as first argument to any widget class? Why is it important?**
    We pass the parent window (root or another frame) as the first argument when creating a widget to specify where that widget should be placed within the GUI hierarchy. This establishes the parent-child relationship between widgets.

21. **Usually, what property do we provide next? Hint: text**
    Usually, the next common property provided is `text`, which sets the text displayed on widgets like labels and buttons.

22. **What are docstring? What is the Syntax to use them? And, where do you use them typically?**
    Docstrings (documentation strings) are multiline strings used to document Python code. They explain what a function, class, module, or method does.
    **Syntax:** They are enclosed in triple quotes (`"""Docstring goes here"""`) immediately after the definition of the documented object.
    **Typical Usage:**
    * At the beginning of a Python module file to describe the module's purpose.
    * Immediately after the `def` line of a function or method to explain its arguments, return value, and behavior.
    * Immediately after the `class` line to describe the class's purpose and its instances.

23. **What is the difference between pack() and grid() method?**
    `pack()` and `grid()` are geometry managers used to organize widgets in a Tkinter window.
    * **`pack()`:** Arranges widgets in a single block, filling available space based on options like `side`, `fill`, and `expand`. It's simpler for basic layouts.
    * **`grid()`:** Arranges widgets in a table-like structure of rows and columns. It offers more precise control over widget placement and alignment in complex layouts.

24. **What arguments can we set in the grid() method?**
    Common arguments for `grid()` include:
    * `row`: The row number for the widget.
    * `column`: The column number for the widget.
    * `rowspan`: The number of rows the widget spans.
    * `columnspan`: The number of columns the widget spans.
    * `padx`: Horizontal padding around the widget.
    * `pady`: Vertical padding around the widget.
    * `sticky`: How the widget should expand within its grid cell (`n`, `s`, `e`, `w`, `nw`, `ne`, `sw`, `se`, `nsew`).
    * `ipadx`: Internal horizontal padding within the widget.
    * `ipady`: Internal vertical padding within the widget.

25. **What is sticky property? What does each of its value - nwes mean together and separately?**
    The `sticky` property in `grid()` controls how a widget expands within its allocated grid cell.
    * **`n` (North):** Aligns the widget to the top of the cell.
    * **`s` (South):** Aligns the widget to the bottom of the cell.
    * **`e` (East):** Aligns the widget to the right of the cell.
    * **`w` (West):** Aligns the widget to the left of the cell.
    * **Combinations:**
        * `nw`: Align top-left.
        * `ne`: Align top-right.
        * `sw`: Align bottom-left.
        * `se`: Align bottom-right.
        * `ew`: Stretch horizontally to fill the cell.
        * `ns`: Stretch vertically to fill the cell.
        * `nsew`: Stretch to fill the cell in all directions.

26. **How to implement rowspan and column span?**
    You implement `rowspan` and `columnspan` as arguments to the `grid()` method of a widget:
    ```python
    widget.grid(row=0, column=0, rowspan=2)  # Spans 2 rows
    another_widget.grid(row=1, column=1, columnspan=3) # Spans 3 columns
    ```

27. **How to create a Text box()? How to display user from being able to write in it?**
    * **Create a Text box:**
      ```python
      import tkinter as tk
      text_box = tk.Text(parent_widget)
      text_box.pack() # or text_box.grid(...)
      ```
    * **Prevent user writing:**
      ```python
      text_box.config(state=tk.DISABLED)
      ```
      To enable writing again: `text_box.config(state=tk.NORMAL)`

28. **How to create a List box? How to fetch the details of the item selected?**
    * **Create a List box:**
      ```python
      import tkinter as tk
      list_box = tk.Listbox(parent_widget)
      list_box.insert(tk.END, "Item 1")
      list_box.insert(tk.END, "Item 2")
      list_box.pack() # or list_box.grid(...)
      ```
    * **Fetch selected item(s):**
      ```python
      selected_indices = list_box.curselection()
      if selected_indices:
          first_selected_index = int(selected_indices[0])
          selected_item = list_box.get(first_selected_index)
          # To get all selected items:
          # selected_items = [list_box.get(int(i)) for i in selected_indices]
      ```

29. **How to create a button?**
    ```python
    import tkinter as tk
    button = tk.Button(parent_widget, text="Click Me")
    button.pack() # or button.grid(...)
    ```
    For themed button:
    ```python
    from tkinter import ttk
    button = ttk.Button(parent_widget, text="Click Me")
    button.pack() # or button.grid(...)
    ```

30. **How to ensure button click triggers a command?**
    You use the `command` argument when creating the button, assigning it the name of the function to be called when the button is clicked:
    ```python
    def button_action():
        print("Button clicked!")

    button = tk.Button(parent_widget, text="Click Me", command=button_action)
    ```

31. **What is after() method in tkinter and after\_cancel()?**
    * **`after(delay_ms, callback=None, *args)`:** This method registers a callback function to be called after a specified `delay_ms` (in milliseconds). It returns an identifier for the scheduled call.
    * **`after_cancel(id)`:** This method cancels a previously scheduled call using the identifier returned by `after()`.

32. **What is try and except? What is Exception as e?**
    `try` and `except` are used for error handling in Python. Code that might raise an exception is placed inside the `try` block. If an exception occurs, the code in the corresponding `except` block is executed.
    `Exception as e` catches any general exception and assigns the exception object to the variable `e`. This allows you to access information about the specific error that occurred (e.g., error message).

33. **How to close the window using the code logic? Hind: destroy()**
    You can close a Tkinter window programmatically using the `destroy()` method of the window object (usually `root` for the main window or the specific tab/window you want to close):
    ```python
    root.destroy()  # To close the main window
    tab_frame.destroy() # To close a specific tab (if it's a toplevel window or frame)
    ```

34. **What is `if __name__ == "__main__":`**
    This is a common Python construct. Code inside this block will only execute when the script is run directly. If the script is imported as a module into another script, the code inside this block will not run. It's often used to run the main part of the application.

35. **Why create an empty `__init__.py` file?**
    An empty `__init__.py` file in a directory tells Python that the directory should be treated as a Python package. This allows you to import modules from that directory using the dot notation (e.g., `import mypackage.mymodule`).

36. **How to display message boxes in GUI?**
    You use the `tkinter.messagebox` module:
    ```python
    from tkinter import messagebox

    messagebox.showinfo("Info", "This is an information message.")
    messagebox.showerror("Error", "An error has occurred!")
    result = messagebox.askyesno("Question", "Do you want to continue?")
    ```

37. **How to display dialog boxes?**
    You can use various modules for dialog boxes, including `tkinter.filedialog` for file selection, `tkinter.colorchooser` for color selection, and `tkinter.simpledialog` for basic input dialogs.

38. **What is the difference between messagebox and simpledialog? What are some common box used in them? Which ones have you used in your code?**
    * **`tkinter.messagebox`:** Used for displaying simple message windows with predefined buttons (e.g., OK, Cancel, Yes, No) to inform or ask the user. Common boxes include `showinfo`, `showerror`, `showwarning`, `askyesno`, `askokcancel`.
    * **`tkinter.simpledialog`:** Used for getting basic input from the user through simple dialog windows. Common boxes include `askinteger`, `askfloat`, `askstring`.
    * **Which ones have you used in your code?** (You need to answer this based on your actual codebase. Examples might be `messagebox.showerror` for displaying error messages or `simpledialog.askstring` for getting a user-defined value).

39. **What do imports like these mean: `import gui.gui as gui`, `import core.system_utils as system_utils`, `import core.ai_client as ai_client`?**
    These are import statements that:
    * `import gui.gui as gui`: Imports the `gui.py` module located in the `gui` directory and assigns it the alias `gui`. You would then access elements within `gui.py` using `gui.ObjectName`.
    * `import core.system_utils as system_utils`: Imports the `system_utils.py` module located in the `core` directory and assigns it the alias `system_utils`. Access elements using `system_utils.FunctionName` or `system_utils.ClassName`.
    * `import core.ai_client as ai_client`: Imports the `ai_client.py` module (or potentially `ai_assistance.py` containing the `AIClient` class) located in the `core` directory and assigns it the alias `ai_client`. Access elements using `ai_client.ClassName` or `ai_client.FunctionName`.
    Using aliases makes the code shorter and can help avoid naming conflicts if you have similarly named elements in different modules.

40. **Why use the word 'root' in your code to represent the window? Can you use anything else?**
    The word 'root' is a common convention used in Tkinter to represent the main top-level window of the application. However, you can use any valid variable name you prefer (e.g., `mainWindow`, `app_window`, `top`). Using 'root' makes the code more readable and understandable for those familiar with Tkinter conventions.

41. **Where have you used List Box in your code?**
    (You need to answer this based on your actual codebase.) Typically, a List Box (`tk.Listbox` or `ttk.Listbox`) might have been used in:
    * **Mini Task Manager Tab:** To display the list of running processes.
    * **Startup Programs Tab:** To show the list of programs that run on system startup.
    * Any other area where a scrollable list of items needs to be presented to the user.

42. **What are f-strings in Python?**
    F-strings (formatted string literals) are a concise and readable way to embed expressions inside string literals for formatting. They are prefixed with an `f` or `F` before the opening quote, and expressions inside curly braces `{}` are evaluated and their values are inserted into the string.
    ```python
    name = "Alice"
    age = 30
    message = f"My name is {name} and I am {age} years old."
    print(message)  # Output: My name is Alice and I am 30 years old.
    ```

43. **What is happening here: `command=lambda: on_terminate_process(tab, system_utils.terminate_process)`?**
    This is setting the `command` option of a button. When the button is clicked:
    * A `lambda` function is executed.
    * This `lambda` function calls the `on_terminate_process` function.
    * It passes two arguments to `on_terminate_process`:
        * `tab`: The current tab or frame where the button is located.
        * `system_utils.terminate_process`: A function (presumably defined in your `system_utils.py` module) that handles the actual process termination logic.

44. **What does `delete()` method here: `tab.process_listbox.delete(0, tk.END)` do?**
    This line calls the `delete()` method on the `process_listbox` widget (which is likely a `tk.Listbox` or `ttk.Listbox` within the `tab`). It deletes items from the list box:
    * `0`: Specifies the index of the first item to delete (starting from the beginning).
    * `tk.END`: Specifies the index of the last item to delete (the end of the list).
    Therefore, this line clears all the items currently displayed in the `process_listbox`.

45. **What is happening here:
    ```python
    tab.grid_rowconfigure(0, weight=1)
    tab.grid_columnconfigure(0, weight=1)
    tab.grid_columnconfigure(1, weight=1)
    ```
    What is the significance of the `weight` argument?**
    These lines configure how rows and columns in the `grid()` layout manager within the `tab` widget should resize when the window is resized.
    * `tab.grid_rowconfigure(0, weight=1)`: Configures the 0th row (the first row) to have a `weight` of 1.
    * `tab.grid_columnconfigure(0, weight=1)`: Configures the 0th column (the first column) to have a `weight` of 1.
    * `tab.grid_columnconfigure(1, weight=1)`: Configures the 1st column (the second column) to have a `weight` of 1.

    **Significance of `weight`:** The `weight` argument determines how extra space is distributed among rows or columns when the window is resized.
    * A `weight` of 0 (the default) means the row or column will not expand.
    * A positive `weight` (like 1) means the row or column will expand proportionally to its weight relative to other weighted rows or columns in the same grid.
    * In this case, the first row will expand vertically when the window height changes, and the first and second columns will expand horizontally when the window width changes, sharing the extra space equally because they have the same weight.

46. **What does `insert` mean: `tab.startup_listbox.insert(tk.END, program)`?**
    This line calls the `insert()` method on the `startup_listbox` widget (likely a `tk.Listbox` or `ttk.Listbox` within the `tab`). It adds a new item to the list box:
    * `tk.END`: Specifies that the new item (`program`) should be inserted at the end of the current list of items.
    * `program`: The data (likely a string representing a startup program) that is being added as a new item to the list box.

47. **What data structures and logic do you use to show chat history in `ai_assistance` tab?**
    The chat history in the `ai_assistance` tab is typically managed using:
    * **Data Structure:** A `tk.Text` widget (`chat_display`) is used to display the conversation.
    * **Logic:**
        * When a user sends a message, the user's input is inserted into the `chat_display`.
        * When the AI responds, the AI's response is also inserted into the `chat_display`.
        * The `insert()` method of the `tk.Text` widget is used to append new messages.
        * The `state` of the `chat_display` is often set to `tk.DISABLED` to prevent the user from directly editing the history, and then temporarily set to `tk.NORMAL` before inserting new text.
        * The `ai_client` object (from `core.ai_client`) internally manages the chat history with the Gemini API. The `get_chat_history_for_display()` method in `ai_client` formats this internal history for display in the `chat_display` widget.

48. **What does `see()` method do: `chat_display.see(tk.END)`?**
    The `see()` method on a `tk.Text` widget makes a given index visible in the widget's view. `chat_display.see(tk.END)` scrolls the `chat_display` widget to the very end, ensuring that the most recently added message is visible to the user. This is commonly used to keep the latest part of the conversation in view as it progresses.

49. **How do you handle events in Tkinter?**
    In Tkinter, you handle events (like button clicks, key presses, mouse movements) by using the `bind()` method on a widget. You specify the event type (e.g., `<Button-1>` for left mouse click, `<Key>` for any key press), and the function (callback) that should be executed when that event occurs on that widget.
    ```python
    import tkinter as tk

    def handle_click(event):
        print("Button clicked at:", event.x, event.y)

    root = tk.Tk()
    button = tk.Button(root, text="Click Me")
    button.bind("<Button-1>", handle_click)
    button.pack()
    root.mainloop()
    ```

50. **What is the difference between tk and ttk modules again, in terms of visual appearance and functionality?**
    * **`tk`:** Provides the basic, standard Tkinter widgets. Their appearance is generally simpler and can look somewhat dated or platform-independent.
    * **`ttk` (Themed Tkinter):** Offers themed versions of the core Tkinter widgets. These widgets are designed to look and feel more native to the operating system on which the application is running (e.g., Windows, macOS, Linux). Functionally, `ttk` widgets often have a slightly more modern API and can provide some enhanced styling options. For basic functionality, they are largely interchangeable with their `tk` counterparts.

51. **How do you make a widget respond to keyboard input?**
    You use the `bind()` method on the widget and bind it to keyboard-related events like `<Key>`, `<KeyPress-a>` (specific key 'a' press), `<Return>` (Enter key), etc. You then define a callback function that takes an event object (containing information about the key press) as an argument.
    ```python
    import tkinter as tk

    def handle_keypress(event):
        print("Key pressed:", event.char)

    root = tk.Tk()
    entry = tk.Entry(root)
    entry.bind("<Key>", handle_keypress)
    entry.pack()
    root.mainloop()
    ```

52. **Why did you choose to use `grid()` for the layout in the AI Assistance tab (or whichever tab you primarily used it in)?**
    (Answer based on your actual choice and reasoning.) For example:
    "We chose `grid()` for the AI Assistance tab because it allows for a more structured and organized layout of the chat display area, the user input field, and the buttons. `grid()` makes it easier to align these elements in rows and columns and to control how they resize relative to each other when the window is resized. This provides a more predictable and user-friendly interface compared to the simpler, block-based arrangement of `pack()`."

53. **Can you walk through the code that creates the AI chat display area? Explain each widget and its configuration.**
    (Provide the relevant code snippet from your `gui.py` and explain each part.) For example:
    ```python
    self.chat_display = tk.Text(tab, state=tk.DISABLED, wrap=tk.WORD)
    self.chat_display.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
    ```
    * `self.chat_display = tk.Text(tab, state=tk.DISABLED, wrap=tk.WORD)`:
        * Creates a `tk.Text` widget named `self.chat_display`.
        * `tab`: Specifies that this text widget is placed within the AI Assistance tab.
        * `state=tk.DISABLED`: Initially makes the text widget read-only, preventing the user from directly typing in the chat history.
        * `wrap=tk.WORD`: Ensures that long lines of text are wrapped at word boundaries to fit within the widget's width.
    * `self.chat_display.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)`:
        * Places the `chat_display` widget in the `grid()` layout of the `tab`.
        * `row=0, column=0`: Positions it in the first row and first column.
        * `columnspan=2`: Makes it span across two columns.
        * `sticky="nsew"`: Causes the widget to expand and fill its entire grid cell in all directions (north, south, east, west) when the window is resized.
        * `padx=5, pady=5`: Adds 5 pixels of padding around the widget in the horizontal and vertical directions.

54. **How does the "Send" button in the AI Assistance tab trigger the communication with the backend? Explain the flow of data.**
    1. **Button Click:** The user clicks the "Send" button.
    2. **`command` Callback:** The `command` option of the button is set to a function (e.g., `_send_user_input`). This function is executed.
    3. **Get User Input:** Inside `_send_user_input`, the text entered by the user in the `ttk.Entry` widget (`user_input_entry.get()`) is retrieved.
    4. **Display User Message:** The user's input is displayed in the `chat_display` widget.
    5. **Call Backend Function:** The `_send_user_input` function then calls a method of the `ai_client` object (which represents the backend AI logic), such as `ai_client.get_response(user_input)`.
    6. **Backend Processing:** The `get_response` method in the backend (likely in `ai_client.py`) takes the user's input, potentially augments it with system information, and sends it to the Gemini API.
    7. **Receive AI Response:** The Gemini API processes the input and returns a response.
    8. **Return to Frontend:** The `get_response` method in the backend returns the AI's response to the `_send_user_input` function in the frontend.
    9. **Display AI Response:** The `_send_user_input` function then calls another function (e.g., `_display_ai_response`) to insert the AI's response into the `chat_display` widget.

55. **How is the chat history updated in the GUI when the AI sends a new response?**
    When the `_display_ai_response` function (or a similar function) in the frontend receives the AI's response:
    1. **Enable Text Widget:** The `state` of the `chat_display` widget is temporarily set to `tk.NORMAL` to allow editing.
    2. **Insert AI Response:** The AI's response (along with an identifier like "SysSKY:") is inserted into the `chat_display` using the `insert(tk.END, ...)` method.
    3. **Disable Text Widget:** The `state` of the `chat_display` is set back to `tk.DISABLED` to prevent further user editing.
    4. **Scroll to Bottom:** The `chat_display.see(tk.END)` method is called to ensure that the newly added response is visible at the bottom of the chat history.

56. **Explain the purpose of the `_clear_chat_history` function and how it interacts with both the frontend display and the backend.**
    The `_clear_chat_history` function is responsible for resetting the chat interface. It performs the following actions:
    1. **Frontend Display:** It clears the content of the `chat_display` widget by setting its state to `tk.NORMAL`, deleting all text from the beginning (`"1.0"`) to the end (`tk.END`), and then setting the state back to `tk.DISABLED`.
    2. **Backend:** It calls the `reset_chat()` method of the `ai_client` object. This method in the backend is responsible for clearing the internal chat history maintained by the Gemini API for the current chat session (by creating a new chat object).
    Essentially, `_clear_chat_history` ensures that both the user's view of the conversation and the AI's memory of the conversation are reset.

57. **In the mini task manager, how is the list of processes populated? Where does this data come from? (Relate it to the backend calls).**
    1. **Frontend Calls Backend:** When the mini task manager tab is opened or periodically updated, the frontend code calls a function in the backend (likely within `system_utils.py` or a related module) to retrieve the list of running processes and their information. This function might be named `get_running_processes()`.
    2. **Backend Retrieves Data:** The `get_running_processes()` function in the backend uses the `psutil` library to get a snapshot of all currently running processes on the system. It then extracts relevant information for each process, such as its name, process ID (PID), CPU usage, memory usage, etc.
    3. **Backend Returns Data:** The backend function formats this process information (e.g., as a list of dictionaries or tuples) and returns it to the frontend.
    4. **Frontend Updates UI:** The frontend code receives this data and then iterates through it. For each process, it inserts a new row into the `tkinter.Treeview` widget (or a `tk.Listbox` if that's used) in the mini task manager tab, displaying the process details in the respective columns.

58. **If you implemented process termination, explain how the frontend signals the backend to terminate a selected process.**
    1. **User Selection:** The user selects a process from the list (e.g., in the `Treeview` or `Listbox`) in the mini task manager tab.
    2. **"Terminate" Button Click:** The user clicks a "Terminate Process" button. The `command` of this button is linked to a function in the frontend (e.g., `on_terminate_process`).
    3. **Get Selected PID:** The `on_terminate_process` function retrieves the Process ID (PID) of the selected process from the `Treeview` or `Listbox`.
    4. **Call Backend Function:** The frontend function then calls a function in the backend (likely in `system_utils.py`), such as `system_utils.terminate_process(pid)`, passing the retrieved PID as an argument.
    5. **Backend Terminates Process:** The `terminate_process` function in the backend uses the `psutil` library to locate the process with the given PID and attempts to terminate it using methods like `process.terminate()` or `process.kill()`.
    6. **Feedback (Optional):** The backend might return a status (success or failure) to the frontend, which could then display a message to the user.

59. **How did you handle potential errors or exceptions that might occur during communication with the backend or while getting system information? (Relate to `try...except` blocks).**
    We used `try...except` blocks in both the frontend and the backend to handle potential errors gracefully:
    * **Backend (e.g., in `ai_client.py` or `system_utils.py`):** When making calls to external APIs (like Gemini) or when using libraries like `psutil` (which might raise exceptions due to permissions or system issues), we enclosed the potentially problematic code in `try` blocks. If an exception occurred, the `except Exception as e:` block would catch it, allowing us to log the error, return an error message to the frontend, or take other appropriate actions to prevent the application from crashing.
    * **Frontend (e.g., in `gui.py`):** When calling backend functions or when updating the UI based on data from the backend, we also used `try...except` blocks. This helps to catch errors that might occur during data transfer or processing and display informative error messages to the user in the GUI (e.g., using `tkinter.messagebox.showerror`) instead of letting the application crash.

60. **How did you manage the state of the GUI (e.g., the chat history, selected processes)?**
    GUI state was managed in several ways:
    * **Chat History:** The chat history in the AI Assistance tab was primarily maintained within the `chat_display` `tk.Text` widget. Each new message (user or AI) was appended to this widget. The backend (`ai_client`) also maintained its own internal history for the AI's context. The `reset_chat()` function synchronized the clearing of both.
    * **Selected Processes (Mini Task Manager):** The currently selected process in the `tkinter.Treeview` (or `Listbox`) was tracked by the widget's internal selection mechanism. The `tree.selection()` or `listbox.curselection()` methods were used to retrieve the index or ID of the selected item when an action (like "Terminate") was initiated.
    * **Widget Properties:** The state of individual widgets (e.g., the `state` of the `chat_display` being `DISABLED` or `NORMAL`) directly reflected the current interaction mode.