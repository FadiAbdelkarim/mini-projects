# Email Sender

A simple Python CLI tool that sends the same email message to a list of recipients pulled from a CSV file.

## Overview

Manually emailing a list of people one by one is tedious and error-prone. This script automates that process: it reads recipient addresses from a CSV file, builds a plain-text email for each one, and sends them all through a single SMTP connection. It's a small, practical example of file I/O, structured data handling, and email automation in Python — built as a hands-on learning project.

## Features

- Reads recipient email addresses from a CSV file (`csv.DictReader`)
- Reads sender credentials from a separate, git-ignored config file (keeps secrets out of version control)
- Builds properly formatted email messages using Python's `email` module
- Batches all messages through a single connection instead of reconnecting per email
- Includes a `dry_run` mode to simulate sending without actually contacting an SMTP server

## Tech Stack

- Python 3 (standard library only — `csv`, `email`, `smtplib`)

## Setup & Installation

1. **Clone the repo** (or navigate to this project folder if it's part of the `mini-projects` monorepo):
   ```bash
   git clone https://github.com/FadiAbdelkarim/mini-projects.git
   cd mini-projects/python/email-sender
   ```

2. **No dependencies to install** — this project only uses the Python standard library.

3. **Set up your config files:**
   - `emails.csv` — a CSV file with a header row `email`, followed by one recipient address per line.
   - `credentials.txt` — two lines: your sender email address, then your SMTP app password (for Gmail, this must be a 16-character [App Password](https://myaccount.google.com/apppasswords), not your regular account password). This file is git-ignored and should never be committed.

4. **Run it:**
   ```bash
   python3 send_emails.py
   ```
   By default, the script runs in `dry_run` mode and only prints what it *would* send. Set `dry_run=False` in the source to send for real.

## Project Structure

```
email-sender/
├── send_emails.py     # Main script
├── emails.csv          # Recipient list (example/template)
├── credentials.txt     # SMTP credentials (git-ignored, not committed)
└── .gitignore
```

## License

This project is licensed under the MIT License.
