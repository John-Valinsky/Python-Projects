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