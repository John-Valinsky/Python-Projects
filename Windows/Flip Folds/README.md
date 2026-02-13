# Background File Copier (Windows)

A lightweight Python utility that asks for a source path, then silently copies all files and folders to a local directory in the background.

When finished, it creates a DONE file and exits automatically.

Designed for simple, unattended file duplication on Windows.


# Features

* Prompts user for a source directory.

* Copies all files and subfolders.

* Runs silently after confirmation.

* Automatically creates a target folder.

* Drops a DONE file when finished.

* Skips copy errors without stopping.


# How It Works

* Launch the script (or compiled .exe).

* Enter a source path when prompted.

* Confirm with any key.

* Console window hides.

* Files are copied in the background.

* A DONE file is created when complete.

* Target files are copied into - "Your Files/" located in the same directory as the script or executable.


# Requirements

* Windows OS

* Python 3.8+ (if running as a script).


# Python Modules Used

* os

* shutil

* sys

* ctypes

* msvcrt

No external dependencies required.


# Limitations

* Windows-only (uses ctypes and msvcrt).

* Errors during copying are silently ignored.

* Existing files may be overwritten.

* No progress indicator or logging.


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