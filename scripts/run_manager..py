#!/usr/bin/env python3
from pathlib import Path
from igigbook_manager.manager import organize_and_export

if __name__ == "__main__":
    master_dir = Path(__file__).resolve().parents[1] / "data" / "master"
    organize_and_export(master_dir)
