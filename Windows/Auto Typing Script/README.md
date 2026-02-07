# Auto Typing Script

A Python-based auto typing tool that simulates human-like typing from a text file into any active application.

It types character by character, supports custom typing speed, shows start/end time, and allows you to stop instantly using the ESC key.


# Features

* Reads text directly from a file.

* Simulates real-time typing.

* Customizable typing speed (with safety limit).

* Cursor setup delay before typing starts.

* Press ESC anytime to stop typing.

* Displays:

	* Start time

	* End time

	* Total duration (H:M:S)

* ASCII banner for a cool terminal look.


# Requirements

* Make sure you have Python 3.x installed.

* Install the dependencies using pip:
```bash
pip install pyautogui keyboard
```


# Note 

* Run the script with Administrator privileges on Windows for keyboard detection to work properly.

* This script controls your keyboard — use responsibly.


# How It Works

* You provide the path to a text file

* Set:

	* Typing speed (seconds per character).

	* Delay time to position your cursor.

* Place the cursor in any app (editor, browser, terminal, etc.).

* The script starts typing automatically.

* Press ESC anytime to stop.


# Usage

* Run the script.

* Enter the text file path.

* Enter typing speed (minimum 0.05 seconds).

* Enter cursor delay time (to position the cursor).


# Typing Speed Rules

* Minimum allowed delay: 0.05 seconds.

* If you enter a faster value, it will auto-adjust.

* Invalid input defaults to 0.1 seconds.


# Example Use Cases

* Typing large notes automatically.

* Demonstrations or presentations.

* Educational simulations.

* Repetitive text input (non-malicious use).

