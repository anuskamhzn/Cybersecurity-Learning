# Python Network Port Scanner

## Overview
A multithreaded TCP port scanner built using Python sockets for educational and authorized security testing.  
The tool identifies open ports, detects common services, and performs basic banner grabbing to fingerprint running services.

## Features
- TCP port scanning using Python sockets
- User-defined port range scanning
- Multithreaded scanning for improved performance
- Service identification using well-known port mapping
- Banner grabbing for HTTP and SSH services
- Timeout handling and thread-safe output
- Ethical use disclaimer

## Technologies Used
- Python 3
- socket
- threading

## Usage
```bash
python scanner.py
