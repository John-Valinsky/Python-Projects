import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def center_window(win, width, height):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

def browse_folder():
    folder = filedialog.askdirectory(title="Select folder to save downloads")
    if folder:
        folder_var.set(folder)

def start_download():
    account_name = account_var.get().strip()
    save_dir = folder_var.get().strip()

 if not account_name:
        messagebox.showerror("Error", "Profile name cannot be empty.")
        return
    if not save_dir:
        messagebox.showerror("Error", "Please select a download folder.")
        return

