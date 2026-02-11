<!-- PROJECT SHIELDS -->
![Repo Size](https://img.shields.io/github/repo-size/John-Valinsky/Python-Projects)
![Last Commit](https://img.shields.io/github/last-commit/John-Valinsky/Python-Projects)
![Open Issues](https://img.shields.io/github/issues/John-Valinsky/Python-Projects)
![Stars](https://img.shields.io/github/stars/John-Valinsky/Python-Projects)


# LAN Terminal Chat

A lightweight local network chat application built with Python sockets and threading.

It lets you run a server and multiple clients in the terminal and chat in real time over your LAN — no external libraries required.

Messages are color-coded for clarity, and everything runs directly in the console.


# Features

* Real-time terminal chat over LAN.

* Multi-client support using threading.

* Color-coded messages.

	* Server messages - red

	* Client messages - green

* Works on any OS that supports Python sockets.

* No external dependencies.

* Simple host / connect workflow.


# Requirements

* Python 3.x

* Devices must be on the same local network.

* Open port: 5555.


# How It Works

* One user starts the server.

* Other users connect as clients.

* All messages are broadcast to everyone.

* yping /quit exits (or shuts down the server).


# Server Mode

When running as server

* Displays your local IP address.

* Listens on port 5555.

* Accepts multiple clients.

* Can send messages directly from the terminal.

* Typing /quit
	
	* Broadcasts shutdown message.

	* Stops the server.


# Client Mode

When running as client:

* Enter the server IP address.

* Connects to the chat instantly.

* Messages:

	* Your messages - green

	* Others / server - red

* Typing /quit

	* Leaves the chat cleanly.


# Networking Notes

* Uses TCP sockets.

* Default port: 5555.

* Server binds to 0.0.0.0 (all interfaces).

* IP auto-detected using UDP socket trick.


# Limitations

* No encryption (plaintext chat).

* LAN only (not internet-exposed).

* No authentication.

* No message history.


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