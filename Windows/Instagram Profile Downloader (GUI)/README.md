<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Python-Projects)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Python-Projects)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Python-Projects)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Python-Projects)

# Instagram Profile Downloader (GUI)

A simple Python Tkinter GUI that lets you download all public content from an Instagram profile using gallery-dl — no terminal commands required.

Just enter a username, choose a folder, and click Start Download.


# Features

* Clean, minimal desktop GUI.

* Downloads photos, videos, and albums from public profiles.

* Choose any folder to save downloads.

* Uses gallery-dl under the hood.

* Automatically centers the app window.

* Live status updates.


# Requirements

Make sure you have the following installed

* Python 3.8+.

* gallery-dl.

* Windows OS (uses cmd to show download progress).

Install gallery-dl via pip:
```bash
pip install gallery-dl
```
Verify installation:
```bash
gallery-dl --version
```


# How It Works

* Enter an Instagram username (without @).

* Select a download folder.

* Click Start Download.

* A command window opens showing download progress.

* The window closes automatically when finished.


# Limitations

* Only public Instagram profiles are supported.

* Private accounts will fail unless you configure gallery-dl authentication.

* This tool does not bypass Instagram restrictions.

* Designed primarily for Windows.


# Customization Ideas

* Add login support via gallery-dl config.

* Progress bar instead of status text.

* Cross-platform support (Linux / macOS).

* Download type selection (posts, reels, stories).


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