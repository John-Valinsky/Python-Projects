<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Python-Projects)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Python-Projects)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Python-Projects)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Python-Projects)


# SMOKE LINK

A simple Tkinter-based GUI tool for generating customized masked URLs with basic validation and shortening features.


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

* Basic input validation.

* API interaction (URL shorteners).


# Ethical Use Policy

This tool demonstrates how URLs can be structured and manipulated.
Using it for deception, phishing, or fraud may violate laws and ethical standards.

* Use responsibly.

* Use for learning and experimentation.

* Do NOT use for malicious purposes


# Disclaimer

This tool is created strictly for educational and research purposes only. It is intended to demonstrate concepts such as GUI development, URL handling, and network requests in Python.

The author will not be responsible for any misuse of this tool.
Any actions taken using this software are solely the responsibility of the user.

By using this project, you agree that:

You will not use it for phishing, fraud, or illegal activities
You understand the ethical implications of manipulating URLs
You accept full responsibility for any consequences resulting from its use

Misuse of this tool may violate local, national, or international laws.