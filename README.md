# Python Security Automation Toolkit

A collection of beginner-friendly Python cybersecurity tools developed to practice security automation, file integrity monitoring, and basic log analysis.

## Tools

### 1. Password Strength Checker
- Checks password length (12+ characters)
- Checks uppercase and lowercase letters
- Checks numbers and special characters
- Displays a score out of 5

### 2. File Integrity Checker
- Calculates SHA-256 file hashes
- Saves a baseline hash
- Detects changes to a file by comparing hashes

### 3. Security Log Analyzer
- Reads a sample security log file
- Identifies failed login events
- Counts failed login attempts
- Generates an alert when three or more failed logins are detected

## Technologies Used

- Python 3
- Visual Studio Code
- SHA-256
- Git and GitHub

## How to Run

Run the following commands from the project folder:

**Password Checker**
```bash
python password_checker.py
```

**File Integrity Checker**
```bash
python file_integrity_checker.py
```

**Log Analyzer**
```bash
python log_analyzer.py
```

No third-party Python packages are required.

## Project Purpose

This project demonstrates basic Python programming, security automation, file integrity verification, and log analysis.

## Disclaimer

These tools are educational prototypes, not production-ready security solutions. Use dummy passwords and sample logs for testing.