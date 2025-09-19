from pathlib import Path

DELETE_EXTS = {".inote", ".idraw", ".plist"}

def classify_name(stem: str, prefix_map: dict) -> str:
    """Return subfolder for master library based on prefix."""
    if stem.startswith(("!", "_")):
        prefix = stem.split(maxsplit=1)[0].replace("!", "_")
        return prefix_map.get(prefix, "Misc")
    return "Misc"

def is_booklist_name(stem: str) -> bool:
    """Detect short cryptic Book List files like crealbk1.pdf."""
    return len(stem) < 12 and stem.islower() and " " not in stem

def normalize_name(file: Path) -> str:
    """Normalize leading ! → _, return safe filename."""
    stem, ext = file.stem, file.suffix
    if stem.startswith("!"):
        stem = "_" + stem[1:]
    return stem + ext
