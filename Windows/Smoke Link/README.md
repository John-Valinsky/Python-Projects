<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Python-Projects)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Python-Projects)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Python-Projects)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Python-Projects)


# SMOKE LINK

A simple Tkinter-based GUI tool for generating customized masked URLs with basic validation and shortening features.

Disclaimer: This project is for educational purposes only (e.g., learning GUI development, URL handling, and networking in Python). Do not use it for phishing, deception, or any illegal activity.


# Features

* Clean and simple Tkinter GUI.

* Automatic URL validation (HTTP status check).

* URL shortening using is.gd.

* Smart protocol handling (https:// auto-added).

* Custom masked URL generation.

* One-click copy to clipboard.

* Input validation (no spaces in custom words).


# Preview
```bash
<======= S M O K E   L I N K S =======>

[ ORIGINAL URL ]
[ CUSTOM DOMAIN ]
[ CUSTOM WORDS ]

→ Generate Link
→ Copy Link
```


# Requirements

* Python 3.x

* Required libraries - pip install requests

* tkinter is usually included with Python by default.


# How to Run

Clone the repository or download the repository

```bash
git clone https://github.com/your-username/smoke-link-generator.git
```

Run the script

```bash
python main.py
```


# How It Works

1 Enter:

Original URL
Custom domain (mask)
Optional keywords


2 The app will:

Normalize URLs (https://)
Check if URLs are reachable
Shorten the original URL


Generate a masked URL format like:

```bash
mask-domain-keywords@shortened-url
```

3 Copy the generated link with one click.


# Important Notes

* Spaces are not allowed in custom words (→ Use - or _ instead).

* URL reachability depends on network conditions.

* URL shortening uses a public API (is.gd).


# Learning Concepts

This project helps you understand:

* GUI development with tkinter.

* HTTP requests with requests.

* Regex usage in Python.

* Clipboard handling.

* Basic input validation

* 
