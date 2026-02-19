def print_ascii_art():
    print("                           _    _                                   ")
    print("                          | |  | | ___   ___  _ __                 ")
    print("                          | |/\\| |/ __| / __|| '__|                ")  # Escape the backslash
    print(r"                          \  /\  /\__ \| (__ | |                   ")
    print(r"                           \/  \/ |___/ \___||_|                   ")
    
    print("-----------------------------------------------------------------------------")
    print("                       ~ ~  By John Valinsky  ~ ~ ")
    print("-----------------------------------------------------------------------------\n")

print_ascii_art()

import os
import fnmatch
import time
import string
from ctypes import windll
import re

def get_available_drives():
    """Returns a list of available drives in the system."""
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(f"{letter}:\\        |")
        bitmask >>= 1
    return drives

def save_output_to_file(output, filename):
    """Saves the output to a text file without ANSI escape codes."""
    try:
        # Remove ANSI escape codes from the output
        cleaned_output = re.sub(r'\033\[[0-9;]*m', '', output)

        with open(filename, "w") as file:
            file.write(cleaned_output)
        print(f"Output has been saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
