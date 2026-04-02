import argparse
from pathlib import Path
from .manager import organize_and_export

def main():
    parser = argparse.ArgumentParser(description="Organize iGigbook library.")
    parser.add_argument(
        "master_dir",
        type=str,
        nargs="?",
        default="data/master",
        help="Path to the master library directory (default: data/master)",
    )
    args = parser.parse_args()
    
    master_dir = Path(args.master_dir).resolve()
    if not master_dir.exists():
        print(f"Error: Master directory '{master_dir}' does not exist.")
        return
    
    organize_and_export(master_dir)

if __name__ == "__main__":
    main()
