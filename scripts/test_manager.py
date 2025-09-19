from igigbook_manager.utils import normalize_name, is_booklist_name

def test_normalize_name():
    from pathlib import Path
    f = Path("!b My Fakebook.pdf")
    assert normalize_name(f) == "_b My Fakebook.pdf"

def test_is_booklist_name():
    assert is_booklist_name("crealbk1")
    assert not is_booklist_name("Classic Real Book")
