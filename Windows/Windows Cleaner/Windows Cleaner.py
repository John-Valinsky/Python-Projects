# Win_Clean
import os
import subprocess

def open_folder(folder_name):
    # Dictionary to map folder names to their paths
    folders = {
        "temp": r"C:\Windows\Temp",
        "%temp%": os.getenv("TEMP"),
        "prefetch": r"C:\Windows\Prefetch"
    }

    # Get the folder path and open it
    folder_path = folders.get(folder_name.lower())
    if folder_path:
        subprocess.Popen(f'explorer {folder_path}')
        print(f"Opened {folder_name} folder.")
    else:
        print("Invalid folder name. Please use 'temp', '%temp%', or 'prefetch'.")

def open_disk_cleanup():
    # Open Disk Cleanup utility
    subprocess.Popen('cleanmgr')
    print("Opened Windows Disk Cleanup.")

# Example usage
open_folder("temp")
open_folder("%temp%")
open_folder("Prefetch")
open_disk_cleanup()
