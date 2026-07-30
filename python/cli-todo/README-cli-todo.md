# CLI To-Do App

A command-line task manager for adding, listing, and deleting to-do items, with tasks persisted to a local JSON file.

## Overview

A lightweight alternative to a full to-do app — everything happens through simple terminal commands, with no database or GUI required. Tasks are stored in a JSON file on disk, so they persist between runs. Built as a hands-on project to practice structuring a real CLI tool around subcommands.

## Features

- **Add** a new task: `python3 todo.py add "buy milk"`
- **List** all tasks, showing completion status: `python3 todo.py list`
- **Delete** a task by its ID: `python3 todo.py delete 2`
- Persistent storage via a local `tasks.json` file (git-ignored, since it's user-specific runtime data)
- Input validation on all commands via `argparse`, including automatic `--help` text for every command

## Tech Stack

- Python 3 (standard library only — `argparse`, `json`)

## Setup & Installation

1. **Clone the repo** (or navigate to this project folder if it's part of the `mini-projects` monorepo):
   ```bash
   git clone https://github.com/FadiAbdelkarim/mini-projects.git
   cd mini-projects/python/cli-todo
   ```

2. **No dependencies to install** — standard library only.

3. **Run it:**
   ```bash
   python3 todo.py add "buy milk"
   python3 todo.py list
   python3 todo.py delete 1
   ```

   See all available commands:
   ```bash
   python3 todo.py --help
   ```

## Project Structure

```
cli-todo/
├── todo.py         # Main script — argument parsing and command logic
└── tasks.json       # Task storage, created automatically on first `add` (git-ignored)
```

## Known Limitations

- Task IDs are currently generated as `len(tasks) + 1`, which can produce duplicate IDs after a task is deleted and a new one is added. A future improvement would use a running counter or UUIDs instead.

## License

This project is licensed under the MIT License.
