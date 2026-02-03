<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Windows/EXE_Firewall_Blocker)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Windows/EXE_Firewall_Blocker)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Windows/EXE_Firewall_Blocker)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Windows/EXE_Firewall_Blocker)

# Windows EXE Firewall Blocker

A Python-based Windows utility that automatically blocks any executable’s internet access by creating inbound and outbound Windows Firewall rules — with automatic admin elevation (UAC).


# Features

* Automatically requests Administrator privileges.

* Blocks both inbound & outbound network traffic.

* Uses native Windows Firewall (no third-party tools).

* Targets a specific executable (not system-wide).

* Simple command-line interface.

* Fast & silent firewall rule creation.


# How It Works

* Checks if the script is running as Administrator.

* If not, it relaunches itself with UAC elevation.

* Prompts the user for the full path to an .exe file.

* Creates two firewall rules:

	* Outbound traffic blocked.

	* Inbound traffic blocked.

* Applies rules using PowerShell (New-NetFirewallRule).


# Requirements

* Windows 10 / 11

* Python 3.7+

* Administrator privileges.

* Windows Defender Firewall enabled.


# Installation
```bash
https://github.com/John-Valinsky/Python-Projects/tree/main/Windows
```
Run the script normally (admin not required initially):
```bash
python blocker.py
```
You’ll be prompted for the executable path

Once confirmed, the script will:

* Elevate permissions (if needed).

* Apply firewall rules.

* Block all network access for that executable.


# Example Firewall Rules Created

* BLOCK OUTBOUND App.exe

* BLOCK INBOUND App.exe

These can be viewed or removed from:

Windows Defender Firewall -> Advanced Settings -> Outbound / Inbound Rules


# How to Remove the Rules

Open PowerShell as Administrator and run:

* Remove-NetFirewallRule -DisplayName "BLOCK OUTBOUND App.exe"

* Remove-NetFirewallRule -DisplayName "BLOCK INBOUND App.exe"


# Security Notes

* This tool does NOT modify the executable.

* No packet interception or monitoring.

* Uses official Windows APIs only.

* Safe for forensic, defensive, and lab environments.


# Use Cases

* Malware analysis & sandboxing.

* Blocking telemetry or unwanted updates.

* Application isolation.

* Digital forensics labs.

* System hardening.


# Codes
```bash
import ctypes
import os
import subprocess
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Auto-elevate if not admin
if not is_admin():
    # Rebuild command line arguments
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    # Relaunch the same script as admin
    ctypes.windll.shell32.ShellExecuteW(
        None,               # hwnd
        "runas",            # verb -> triggers UAC
        sys.executable,     # python.exe path
        params,             # script + arguments
        None,               # working directory
        1                   # SW_NORMAL (show window)
    )
    sys.exit(0)            # exit the non-admin instance

# --- Banner ---
print()
print("          ___   ___ _    ___   ___ _  _____ ___")
print("         | __| | _ ) |  / _ \\ / __| |/ / __| _ \\")
print("         | _|  | _ \\ |_| (_) | (__| ' <| _||   /")
print("         |_|   |___/____\\___/ \\___|_|\\_\\___|_|_\\")
print()
print(" ======================================================")
print("                  -- John Valinsky --")
print(" ======================================================")
print(" Enter the FULL path of the executable to block")
print(" Example: C:\\Program Files\\Program.exe\n")

# --- User input ---
exe_path = input(" EXE Path: ").strip().strip('"')

# Remove trailing dot if user adds one
if exe_path.endswith("."):
    exe_path = exe_path[:-1]

if not os.path.isfile(exe_path):
    print("\nExecutable not found. Exiting.")
    input("Press Enter to exit...")
    sys.exit(1)

exe_name = os.path.basename(exe_path)

print("\nBlocking executable:")
print(exe_path)
print()

# --- Firewall rule function ---
def add_firewall_rule(direction):
    rule_name = f"BLOCK {direction.upper()} {exe_name}"
    cmd = [
        "powershell",
        "-NoProfile",
        "-Command",
        f"New-NetFirewallRule "
        f"-DisplayName '{rule_name}' "
        f"-Direction {direction} "
        f"-Program '{exe_path}' "
        f"-Action Block "
        f"-Profile Any"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Apply both outbound and inbound rules
add_firewall_rule("outbound")
add_firewall_rule("inbound")

print("\nFirewall rules applied successfully.")
input("\nPress Enter to exit...")
```


# License

MIT License

Copyright (c) 2026 John Valinsky

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.