# Set Alarm

A command-line alarm clock that waits until a chosen time, then plays a sound from macOS's built-in system sounds.

## Overview

A simple terminal-based alarm clock: enter a target time and pick a sound from a short menu, and the script waits (checking the clock every second) until that time arrives, then plays your chosen sound. Adapted from a Windows-only version of this project to run natively on macOS using the built-in `afplay` command instead of `winsound`.

## Features

- Prompts for and validates a target alarm time in `HH:MM` format
- Menu-driven sound selection from macOS's built-in system sounds
- Waits in a lightweight polling loop until the target time is reached
- Plays the selected sound via macOS's `afplay` command
- Friendly, re-prompting input validation on both the time and sound menu — invalid input doesn't crash the program

## Tech Stack

- Python 3 (standard library — `datetime`, `time`, `subprocess`)
- macOS `afplay` command (used for audio playback; this project is macOS-specific)

## Setup & Installation

1. **Clone the repo** (or navigate to this project folder if it's part of the `mini-projects` monorepo):
   ```bash
   git clone https://github.com/FadiAbdelkarim/mini-projects.git
   cd mini-projects/python/set-alarm
   ```

2. **No dependencies to install** — standard library only. Requires macOS (uses the built-in `afplay` command and `/System/Library/Sounds/`).

3. **Run it:**
   ```bash
   python3 alarm.py
   ```
   Follow the prompts to set a time and choose a sound. Leave the terminal open — the program needs to keep running to trigger the alarm.

## Project Structure

```
set-alarm/
└── alarm.py     # Main script — time input, sound selection, wait loop, playback
```

## Known Limitations

- macOS only (relies on `afplay` and `/System/Library/Sounds/`).
- Time comparison doesn't account for day rollover — if the target time has already passed today, the alarm won't correctly wait until tomorrow.

## License

This project is licensed under the MIT License.
