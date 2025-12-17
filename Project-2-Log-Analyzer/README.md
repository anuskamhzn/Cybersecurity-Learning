# Log Analyzer for Suspicious Login Attempts

## Overview
This project is a Python-based log analysis tool designed to identify suspicious IP addresses by analyzing authentication log files. The script detects repeated failed login attempts, which may indicate brute-force attacks or unauthorized access attempts.

This project is intended for **entry-level cybersecurity learners** to gain hands-on experience with log analysis and threat detection.

---

## Features
- Parses system authentication log files
- Extracts IP addresses from failed login attempts
- Counts repeated failures per IP address
- Flags suspicious IPs exceeding a defined threshold
- Simple and efficient implementation using Python

---

## Technologies Used
- Python 3
- File Handling
- `collections.Counter`
- Basic Cybersecurity Concepts
- Log Analysis

---

## Sample Log Format
The script expects log entries containing the phrase:
Security Alert Report
------------------------------
[!] Suspicious IP Detected: 192.168.1.10 (3 failed attempts)

Summary
Total Failed Attempts: 4
Unique IP Addresses: 2

---

## How to Run
1. Clone the repository: git clone https://github.com/anuskamhzn/Cybersecurity-Learning.git
2. cd Project-2-Log-Analyzer
3. ## Usage
```bash
python scanner.py