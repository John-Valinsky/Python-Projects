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

 url = f"https://www.instagram.com/{account_name}/"
 cmd = ["gallery-dl", "-d", save_dir, url]

 status_var.set("Downloading...")
 root.update_idletasks()

     try:
        # Open in a new cmd window, show output, then auto-close
        subprocess.run(f'start cmd /c {" ".join(cmd)}', shell=True)
        status_var.set(f"Download complete! Saved in:\n{save_dir}")
    except Exception as e:
        status_var.set(f"Download failed!\n{e}")

root = tk.Tk()
root.title("John Valinsky")
center_window(root, 500, 250)
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Instagram Username:", font=("Arial", 11)).grid(row=0, column=0, sticky="w")
account_var = tk.StringVar()
tk.Entry(frame, textvariable=account_var, width=30).grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Save Folder:", font=("Arial", 11)).grid(row=1, column=0, sticky="w")
folder_var = tk.StringVar()
tk.Entry(frame, textvariable=folder_var, width=30).grid(row=1, column=1, padx=10, pady=5)
tk.Button(frame, text="Browse", command=browse_folder).grid(row=1, column=2, padx=5)



