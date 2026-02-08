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