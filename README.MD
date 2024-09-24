# Port Scanner Tool

## Description
This is a Python-based Port Scanner tool designed for cybersecurity professionals and networking enthusiasts. It scans for open TCP and UDP ports on a target machine and provides details on the services running on those ports. The tool also supports multi-threading to speed up the scanning process.

## Features
- **TCP/UDP Port Scanning**: Supports scanning for both TCP and UDP ports.
- **Service Identification**: Identifies the service running on each open port using a predefined list.
- **Ping Target**: Verifies if the target is up and reachable using a `ping` command before scanning.
- **Multi-threading**: Uses Python's `ThreadPoolExecutor` to scan multiple ports simultaneously, increasing efficiency.
- **Customizable**: Allows users to specify a target IP/hostname, protocol, and specific port to scan, or to scan all well-known ports.
- **Colorful Output**: Uses the `colorama` library to display scan results with colored output in the terminal.

## Technologies Used
- **Language**: Python
- **Key Libraries**:
  - `socket`: For managing network connections and port scanning.
  - `concurrent.futures (ThreadPoolExecutor)`: For multi-threading and speeding up port scanning.
  - `os`: To handle the `ping` command for checking if the target is reachable.
  - `optparse`: To handle command-line arguments and provide easy customization.
  - `colorama`: To provide colorful output in the terminal, enhancing the user experience.

## Prerequisites
Make sure you have Python installed, and install the required libraries by running:
```bash
pip install -r requirements.txt

The required libraries:

• socket
• concurrent.futures
• os
• optparse
• colorama
How to Use
1.Clone the repository:
```
git clone https://github.com/hemaabokila/pscan.git
cd pscan
pip install -r requirements.txt
sudo mv pscan.py /usr/bin/pscan && chmod +x /usr/bin/pscan
```
2.Run the script with the following options:
```
pscan -t <target> -p <port> -P <protocol>

```
> ![Screenshot_2024-09-24_09-19-57](https://github.com/user-attachments/assets/11f84875-9adf-4a8c-8878-8573ff500d5d)
Options:
• -t or --target: Target IP address or hostname (required).
• -p or --port: Port number to scan (optional, leave empty to scan all well-known ports).
• -P or --protocol: Protocol to use, 't' for TCP (default) or 'u' for UDP (optional).
Example:
To scan a target machine (e.g., 192.168.1.1) on port 80 using TCP:
```
pscan -t 192.168.1.1 -p 80 -P t
```
To scan all well-known TCP ports on a target machine:
```
pscan -t 192.168.1.1
```
Ports and Services
The tool comes with a list of common ports and the services typically associated with them, including:

• 22: SSH
• 80: HTTP
• 443: HTTPS
• 3306: MySQL
• And many more...
Example Output
After scanning, the tool will show results like this (for TCP protocol)
```
TCP Port 22: OPEN (Service: SSH)
TCP Port 80: OPEN (Service: HTTP)
```
For UDP protocol, it will show results like this:
```
UDP Port 53: OPEN
```
Author
Developed by Ibrahem abo kila
Feel free to reach out for any questions or suggestions!
• LinkedIn: Connect with me
• YouTube: Watch my videos




