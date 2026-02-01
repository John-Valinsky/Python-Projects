<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Python-Projects)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Python-Projects)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Python-Projects)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Python-Projects)

# Python Socket HTTP Client

A simple Python socket-based HTTP client that demonstrates how to manually send an HTTP request and receive a response from a web server using low-level networking.

This project connects to google.com over port 80, sends a raw HTTP GET request, and prints the server’s response.


# About the Project

This script helps you understand:

* How TCP sockets work in Python

* How HTTP requests look at the raw protocol level.

* Client–server communication without external libraries.

* Basics of networking useful for cybersecurity & forensics.

No frameworks. No abstractions. Just pure sockets.


# How It Works

* Creates a TCP socket.

* Connects to www.google.com on port 80.

* Sends a raw HTTP GET / request.

* Receives the server response.

* Prints the HTML content returned by the server.

* Closes the connection.


# Codes
```bash
import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()
```


# Requirements

* Python 3.x

* Internet connection

* Works on:

	* Windows

	* Linux


# How to Run
```bash
python socket_http_client.py
```
Expected output:

* Raw HTTP response headers

* HTML content of Google’s homepage (or a redirect response)


# Important Notes

