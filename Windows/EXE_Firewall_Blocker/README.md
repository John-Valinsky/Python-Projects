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


# Installation
```bash
https://github.com/John-Valinsky/Python-Projects/tree/main/Windows
```
Run the script normally (admin not required initially):
```bash
python blocker.py
```
You’ll be prompted for the executable path

Once confirmed, the script will:

* Elevate permissions (if needed).

* Apply firewall rules.

* Block all network access for that executable.


# Example Firewall Rules Created

* BLOCK OUTBOUND App.exe

* BLOCK INBOUND App.exe

These can be viewed or removed from:

Windows Defender Firewall -> Advanced Settings -> Outbound / Inbound Rules


# How to Remove the Rules

Open PowerShell as Administrator and run:

* Remove-NetFirewallRule -DisplayName "BLOCK OUTBOUND App.exe"

* Remove-NetFirewallRule -DisplayName "BLOCK INBOUND App.exe"


# Security Notes

* This tool does NOT modify the executable.

* No packet interception or monitoring.

* Uses official Windows APIs only.

* Safe for forensic, defensive, and lab environments.


# Use Cases

* Malware analysis & sandboxing.

* Blocking telemetry or unwanted updates.

* Application isolation.

* Digital forensics labs.