<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Windows)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Windows)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Windows)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Windows)

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

* Content drafting assistance.


# Safety Notes

* Do NOT use this for spamming or violating platform policies.

* Always know where your cursor is before typing starts.

* Keep the ESC key ready.


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