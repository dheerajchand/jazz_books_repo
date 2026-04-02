# iGigbook Manager Overview

iGigbook Manager is a Python-based utility designed to organize and manage a large collection of music PDFs and their associated metadata files (e.g., bookmarks, inotes, idraws) for use with applications like iGigbook.

## Core Features
- **Categorization:** Automatically organizes files into predefined categories based on filename prefixes.
- **Normalization:** Cleans up filenames by converting specific prefixes (e.g., `!` to `_`).
- **Sync Flat Folder:** Creates a flat "sync" folder containing only the files needed for your mobile device, including an automatically generated `library_index.csv`.
- **Cleanup:** Identifies and removes known junk files (e.g., `.inote`, `.idraw`, `.plist` if they aren't needed).
- **Archiving:** Safely moves unclassified or stray files into an archive folder rather than deleting them.

## Directory Structure
- `data/master`: Your primary, organized library.
- `data/sync`: A flat folder ready for syncing to your device.
- `data/archive`: Contains unclassified and junk files moved out of the master library.
- `igigbook_manager/`: The core logic of the application.
- `scripts/`: Helper scripts for running the manager.
- `tests/`: A `pytest` suite for ensuring functionality.

## Getting Started
To run the manager with the default settings:
```bash
python3 main.py
```
This will process the files in `data/master`.
