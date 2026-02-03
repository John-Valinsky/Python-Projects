# Windows EXE Firewall Blocker

A Python-based Windows utility that automatically blocks any executable’s internet access by creating inbound and outbound Windows Firewall rules — with automatic admin elevation (UAC).


# Features

* Automatically requests Administrator privileges.

* Blocks both inbound & outbound network traffic.

* Uses native Windows Firewall (no third-party tools).

* Targets a specific executable (not system-wide).

* Simple command-line interface.

* Fast & silent firewall rule creation.


# How It Works

* Checks if the script is running as Administrator.

* If not, it relaunches itself with UAC elevation.

* Prompts the user for the full path to an .exe file.

* Creates two firewall rules:

	* Outbound traffic blocked.

	* Inbound traffic blocked.

* Applies rules using PowerShell (New-NetFirewallRule).


# Requirements

* Windows 10 / 11

* Python 3.7+

* Administrator privileges.

* Windows Defender Firewall enabled.




