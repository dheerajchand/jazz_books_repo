import os
import shutil
from pathlib import Path

# Root of your master library
MASTER = Path(".")

# Destination for sync-safe copies
SYNC_DIR = MASTER / "igig_sync"
SYNC_DIR.mkdir(exist_ok=True)

# File types we want to ignore
DELETE_EXTS = {".bookmark", ".inote", ".idraw", ".plist"}

def is_booklist_name(stem: str) -> bool:
    """
    Detect short cryptic names (Book List files like crealbk1.pdf).
    Rule of thumb: < 12 chars, all lowercase, no spaces.
    """
    return len(stem) < 12 and stem.islower() and " " not in stem

def safe_name(file: Path) -> str:
    """
    Return safe filename for sync.
    Replace leading !prefix with _prefix.
    """
    stem, suffix = file.stem, file.suffix
    if stem.startswith("!"):
        parts = stem.split(maxsplit=1)
        prefix = parts[0].replace("!", "_")  # e.g. !b -> _b
        rest = parts[1] if len(parts) > 1 else ""
        new_stem = f"{prefix} {rest}".strip()
        return new_stem + suffix
    return file.name

def export_file(file: Path):
    # Delete junk files
    if file.suffix in DELETE_EXTS:
        print(f"Skipping junk file: {file.name}")
        return

    # Only process PDFs
    if file.suffix.lower() != ".pdf":
        print(f"Skipping non-PDF: {file.name}")
        return

    # Detect Book List files
    if is_booklist_name(file.stem):
        new_name = file.name
    else:
        new_name = safe_name(file)

    dest = SYNC_DIR / new_name
    print(f"Copying {file.name} -> {dest.name}")
    shutil.copy2(file, dest)

# Process files (non-recursive; just top level)
for f in MASTER.iterdir():
    if f.is_file():
        export_file(f)

print("\nExport complete!")
print(f"Sync-safe files are in: {SYNC_DIR}")
