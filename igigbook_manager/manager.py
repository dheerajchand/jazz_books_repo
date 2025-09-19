import shutil
import csv
from pathlib import Path
from .categories import PREFIX_MAP
from .utils import classify_name, is_booklist_name, normalize_name, DELETE_EXTS

def organize_and_export(master_dir: Path):
    """Organize master library and export sync copy."""

    sync_dir = master_dir.parent / "sync"      # keep sync outside master
    archive_dir = master_dir.parent / "archive" / "unclassified"
    sync_dir.mkdir(exist_ok=True, parents=True)
    archive_dir.mkdir(exist_ok=True, parents=True)

    csv_path = sync_dir / "library_index.csv"
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Prefix", "Category", "OriginalPath", "MasterPath", "SyncName"])

        for file in master_dir.rglob("*"):
            if not file.is_file():
                continue

            ext = file.suffix.lower()

            # Delete junk outright
            if ext in DELETE_EXTS:
                print(f"Deleting junk: {file}")
                file.unlink()
                continue

            if ext not in [".pdf", ".bookmark"]:
                # Move any other strays into archive
                dest = archive_dir / file.name
                print(f"Archiving unclassified file: {file} -> {dest}")
                shutil.move(str(file), str(dest))
                continue

            stem = file.stem
            new_name = normalize_name(file)

            # Handle Book List files
            if is_booklist_name(stem):
                master_dest = master_dir / "BookList"
                master_dest.mkdir(exist_ok=True)
                master_file = master_dest / file.name
                sync_name = file.name
            else:
                category = classify_name(stem, PREFIX_MAP)
                master_dest = master_dir / category
                master_dest.mkdir(exist_ok=True)
                master_file = master_dest / new_name
                sync_name = new_name

            # Move file in master library (if not already there)
            if file.resolve() != master_file.resolve():
                print(f"Moving {file} -> {master_file}")
                shutil.move(str(file), str(master_file))
            else:
                print(f"Already organized: {file}")

            # Only copy to sync if it's a PDF, or a bookmark with matching PDF
            if ext == ".pdf" or (ext == ".bookmark" and master_file.with_suffix(".pdf").exists()):
                sync_dest = sync_dir / sync_name
                print(f"Copying to sync: {sync_dest}")
                shutil.copy2(master_file, sync_dest)

                # Write to index CSV
                prefix = stem.split()[0] if stem.startswith(("_", "!")) else ""
                category = classify_name(stem, PREFIX_MAP)
                writer.writerow([prefix, category, str(file), str(master_file), sync_name])

    print("\n✅ Done!")
    print(f"Master organized under: {master_dir}")
    print(f"Sync-ready flat folder: {sync_dir}")
    print(f"Unclassified files archived under: {archive_dir}")
    print(f"CSV index written to: {csv_path}")
