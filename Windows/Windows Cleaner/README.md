# Win_Clean

Win_Clean is a lightweight Python utility for Windows that quickly opens common system cleanup folders and launches the built-in Disk Cleanup tool. It’s designed for fast access to temp files and maintenance locations without digging through directories manually.


# Features

* Open Windows Temp folder.

* Open User %TEMP% folder.

* Open Windows Prefetch folder.

* Launch Windows Disk Cleanup (cleanmgr).

* Simple, readable Python script.

* No external dependencies.


# Supported Folders

* temp - C:\Windows\Temp

* %temp% - User temporary files

* prefetch - C:\Windows\Prefetch


# Requirements

* Windows OS.

* Python 3.x.

* Administrator privileges recommended (for full access).


# Notes

* This tool does not delete files automatically — it only opens folders and utilities.

* Be careful when deleting system files; remove only what you recognize.

* Some folders may require administrator permissions to access.


# Use Cases

* Quick system cleanup.

* Maintenance scripts.

* IT support workflows.

* Learning subprocess automation in Python.


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