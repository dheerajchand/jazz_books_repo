#!/usr/bin/env python3
import sys
from pathlib import Path

# Add root directory to sys.path
root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from igigbook_manager.manager import organize_and_export

if __name__ == "__main__":
    master_dir = root_dir / "data" / "master"
    organize_and_export(master_dir)
