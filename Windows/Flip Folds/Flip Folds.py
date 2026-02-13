# file_copier.py
# Asks user for a path, then copies files & folders in background.
# Creates a DONE file when finished and exits automatically.

import os
import shutil
import sys
import ctypes
import msvcrt

def hide_console():
    """Hide the console window (only works on Windows)."""
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hwnd = kernel32.GetConsoleWindow()
    if hwnd:
        user32.ShowWindow(hwnd, 0)  # 0 = hide

def wait_for_keypress():
    """Pause before hiding so user sees the entered path."""
    print("\nPress any key to start copying in background...")
    msvcrt.getch()

def copy_files(source_dir, target_dir):
    """Copy everything from source_dir into target_dir."""
    os.makedirs(target_dir, exist_ok=True)

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)

        try:
            if os.path.isdir(source_item):
                shutil.copytree(source_item, target_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, target_item)
        except:
            pass  # skip errors silently

def main():
    # Ask for path in console
    source_dir = input("PATH /:> ").strip()

    if not os.path.exists(source_dir):
        print("Path not found. Exiting...")
        return

    # Show path back to user
    print(f"\nSource path set to: {source_dir}")
    wait_for_keypress()

    # Hide console and copy in background
    hide_console()

    # Target folder = "Your Files" next to .exe
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    target_dir = os.path.join(base_dir, "Your Files")

    copy_files(source_dir, target_dir)

    # Create DONE file next to exe
    done_file = os.path.join(base_dir, "DONE")
    with open(done_file, "w", encoding="utf-8") as f:
        f.write("Copy completed successfully.")

if __name__ == "__main__":
    print(r"""
    ______ _ _        ______    _     _     
    |  ___| (_)       |  ___|  | |   | |    
    | |_  | |_ _ __   | |_ ___ | | __| |___ 
    |  _| | | | '_ \  |  _/ _ \| |/ _` / __|
    | |   | | | |_) | | || (_) | | (_| \__ \
    \_|   |_|_| .__/  \_| \___/|_|\__,_|___/
              | |                           
              |_|                           
    """)
    print("       ================================")
    print("        - - - - John Valinsky - - - -")
    print("       ================================")
    print(" ")

    main()
