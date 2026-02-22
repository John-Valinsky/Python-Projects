<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Python-Projects)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Python-Projects)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Python-Projects)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Python-Projects)

# Windows File & Directory Search Tool (Python)

A simple but powerful Windows-only Python search utility that scans drives or directories for files or folders matching a wildcard pattern. It features an ASCII art banner, colored terminal output, timing stats, and optional export to a text file.


# Features

* Windows drive detection (automatically lists available drives).

* Search files or directories using wildcard patterns (* , ?).

* Execution time tracking.

* Color-coded terminal output (red highlights).

* Optional export to .txt file.


# Preview
```bash
                           _    _                                   
                          | |  | | ___   ___  _ __                 
                          | |/\| |/ __| / __|| '__|                
                          \  /\  /\__ \| (__ | |                   
                           \/  \/ |___/ \___||_|                   
-----------------------------------------------------------------------------
                       ~ ~  By John Valinsky  ~ ~
-----------------------------------------------------------------------------
```

# How It Works

* Detects all available Windows drives using ctypes.

* Prompts the user for:

	* Search pattern (example: *report*).

	* Directory or drive (defaults to C:\).

	* Search type: file or directory.

* Recursively scans using os.walk.

* Displays results and total search time.


# Requirements

* Windows OS.

* Python 3.7+

Built-in Libraries Used

* os

* fnmatch

* time

* string

* re

* ctypes (Windows API)

This script will not work on macOS or Linux due to Windows-specific drive detection.


# Limitations

* Case-sensitive matching

* No multithreading (large drives may take time)

* Windows-only support


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