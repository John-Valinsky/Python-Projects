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
