import tkinter as tk
from tkinter import messagebox
import requests
import re

# Function: Center window on any screen
def center_window(win, width, height):
    win.update_idletasks()  # Update "requested size" before getting screen info
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# Function: Check if a URL is reachable
def url_checker(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if 200 <= response.status_code < 400:
            return f"[✓] URL is reachable (HTTP {response.status_code})"
        else:
            return f"[!] URL not reachable (HTTP {response.status_code})"
    except requests.RequestException as e:
        return f"[!] Error reaching URL: {e}"

# Function: Auto-add https:// if missing
def add_protocol(url):
    if not url:
        return url
    if re.match(r"^https?://", url):
        return url
    return f"https://{url}"

# Main processing function
def generate_maskphish():
    # Clear previous output
    result_box.delete("1.0", tk.END)

    # Get user inputs
    phish = add_protocol(entry_phish.get().strip())
    mask = add_protocol(entry_mask.get().strip())
    words = entry_words.get().strip()

    # Your generation logic (example)
    if words:
        final_url = f"{mask}-{words}@{phish}"
    else:
        final_url = f"{mask}@{phish}"

    result_box.insert(tk.END, final_url)

    if not phish or not mask:
        messagebox.showerror("Error", "Please enter both Phishing URL and Mask Domain.")
        return

    # Check URLs
    phish_status = url_checker(phish)
    mask_status = url_checker(mask)

    # Shorten using is.gd
    try:
        short = requests.get(f"https://is.gd/create.php?format=simple&url={phish}").text.strip()
        shorter = short.replace("https://", "")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")
        return

    # Build final URL
    if not words:
        final_url = f"{mask}@{shorter}"
    elif " " in words:
        messagebox.showwarning("Invalid", "Spaces are not allowed in social engineering words. \n\n Use '-' or '_' instead.")
        final_url = f"{mask}@{shorter}"
    else:
        final_url = f"{mask}-{words}@{shorter}"

    # Save result for copy button
    result_box.insert(tk.END,
    f"Final MaskPhish URL:\n{final_url}\n\nPhish Status: {phish_status}\nMask Status: {mask_status}")
    copy_button.config(state=tk.NORMAL)
    copy_button.url_to_copy = final_url

# Function: Copy URL to clipboard
def copy_to_clipboard():
    if hasattr(copy_button, "url_to_copy"):
        root.clipboard_clear()
        root.clipboard_append(copy_button.url_to_copy)
        root.update()
        messagebox.showinfo("Copied", "URL Copied to Clipboard!")

# Create main window
root = tk.Tk()
root.title("Smoke Link | 2025 | John Valinsky ")
center_window(root, 400, 500)  # <-- Centers the window no matter the screen size
root.resizable(False, False)

tk.Label(root, text="<======= S M O K E   L I N K =======>", font=("Segoe UI", 12, "bold"), fg="black").pack(pady=5)

# Phishing URL input
tk.Label(root, text="~|| ORIGINAL URL ||~", font=("Segoe UI", 12, "bold"), fg="blue").pack(pady=5)
entry_phish = tk.Entry(root, width=60)
entry_phish.pack()

# Mask Domain input
tk.Label(root, text="~|| CUSTOMIZE DOMAIN NAME ||~", font=("Segoe UI", 12, "bold"), fg="green").pack(pady=5)
entry_mask = tk.Entry(root, width=60)
entry_mask.pack()

# Social engineering words
tk.Label(root, text="~|| CUSTOMIZE WORDS ||~", font=("Segoe UI", 12, "bold"), fg="red").pack(pady=5)
entry_words = tk.Entry(root, width=60)
entry_words.pack()

# Generate button
tk.Button(root, text="Generate Link", command=generate_maskphish, bg="black", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=10)

# Scrollable result display
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

result_box = tk.Text(
    result_frame,
    wrap="word",
    yscrollcommand=scrollbar.set,
    height=8,
    width=45,
    fg="black",
    font=("Segoe UI", 11)
)
result_box.pack(side="left")
scrollbar.config(command=result_box.yview)

# Copy button
copy_button = tk.Button(root, text="Copy Link", command=copy_to_clipboard, fg="white", bg="black", font=("Segoe UI", 9, "bold"))
copy_button.pack(pady=5)

root.mainloop()
