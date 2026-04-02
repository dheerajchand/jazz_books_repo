# How to Modify the Scripts

The iGigbook Manager is designed to be easily extensible and customizable.

## Modifying Categories
To change how files are categorized, edit `igigbook_manager/categories.py`. 

### Add a New Prefix
If you have a new category (e.g., `Jazz`), you can add a prefix:
```python
PREFIX_MAP = {
    "_j": "Jazz",
    # existing prefixes...
}
```

### Map Multiple Prefixes to One Category
You can map multiple codes to the same folder:
```python
PREFIX_MAP = {
    "_c": "Classical",
    "_cu": "Classical",
    # both will move to data/master/Classical
}
```

## Changing Junk File Rules
In `igigbook_manager/utils.py`, modify the `DELETE_EXTS` set:
```python
DELETE_EXTS = {".inote", ".idraw", ".plist", ".tmp"}
```

## Customizing the Sync Folder
If you want to change where the sync folder is created or what it includes, edit `igigbook_manager/manager.py`'s `organize_and_export` function.

### Changing the Sync Path:
Modify the following line:
```python
sync_dir = master_dir.parent / "sync"
```

## Running Tests
After making changes, verify they didn't break anything:
```bash
pytest
```
Add new tests to `tests/test_manager.py` for any new logic you implement.
