import tkinter as tk
from tkinter import messagebox
   
def display_error_message(message):
    """Displays an error message in a popup window."""
    messagebox.showerror("Error", message)

if __name__ == '__main__':
    # Simple test
    root = tk.Tk()
    root.withdraw()
    display_error_message("This is a test error message!")