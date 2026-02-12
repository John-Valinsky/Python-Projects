import os
import sys

print(r"""
    ┏┓  ┓ ┓      ┓ ┏•      ┓ 
    ┣ ┏┓┃┏┫┏┓┏┓  ┃┃┃┓┓┏┓┏┓┏┫┏
    ┻ ┗┛┗┗┻┗ ┛   ┗┻┛┗┗┗┻┛ ┗┻┛ """)
print("================================")
print("- - - - By John Valinsky - - - -")
print("================================")

# ==== USER INPUTS ====
base_name = input("</ Folder series name: ")
quantity = int(input("</ Number of folders: "))
location = input("</ Folder location: ")
# =====================

# If location is "#", use current script/exe directory
if location.strip() == "#":
    location = os.path.dirname(os.path.abspath(sys.argv[0]))

# Create location folder if not exists
os.makedirs(location, exist_ok=True)

print(f"\nCreating folders in: {location}\n")

# Create missing folders only
for i in range(1, quantity + 1):
    folder_name = f"{base_name}-{i}"
    folder_path = os.path.join(location, folder_name)

    if os.path.exists(folder_path):
        print(f"Skipped (already exists): {folder_name}")
        continue

    try:
        os.makedirs(folder_path)
        print(f"Created: {folder_name}")
    except Exception as e:
        print(f"Error creating {folder_name}: {e}")

input("\nDone! Press Enter to exit...")
