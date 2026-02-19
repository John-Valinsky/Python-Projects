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

def search_items(keyword, location, search_type):
    """Searches for files or directories matching the keyword."""
    try:
        print(f"\nSearching for {search_type}s with pattern '{keyword}' in '{location}'...\n")
        start_time = time.time()  # Record start time
        found_items = []
        output = ""  # Initialize output variable

        # Walk through the directory and subdirectories
        for root, dirs, files in os.walk(location):
            items = dirs if search_type == "directory" else files  # Determine whether to search files or directories
            for item in items:
                if fnmatch.fnmatch(item, keyword):  # Case-sensitive match
                    found_items.append(os.path.join(root, item))

  # Print the results in red
        if found_items:
            output += f"\033[31m{search_type.capitalize()}s found:\033[0m\n"
            print(f"\033[31m{search_type.capitalize()}s found:\033[0m")  # Red text
            print("=================");
            for item in found_items:
                output += f"{item}\n"
                print(f"\033[31m{item}\033[0m")  # Red text for each item
        else:
            output += f"\033[31mNo {search_type}s found with the given pattern.\033[0m\n"
            print(f"\033[31mNo {search_type}s found with the given pattern.\033[0m")  # Red text

   # Display total time taken
        end_time = time.time()
        time_taken = f"\n\033[31mSearch completed in {end_time - start_time:.2f} seconds.\033[0m"
        output += time_taken
        print(time_taken)  # Red text

        return output  # Return output to be saved later

    except Exception as e:
        print(f"An error occurred: {e}")


