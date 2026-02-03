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
