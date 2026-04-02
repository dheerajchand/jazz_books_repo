# Scripts Documentation

The `igigbook_manager` provides several ways to organize your library.

## Primary Entry Points

### `main.py`
The standard entry point at the root. Run it to process your `data/master` directory:
```bash
python3 main.py
```

### `python3 -m igigbook_manager`
Run the package as a module. You can optionally pass a custom directory:
```bash
python3 -m igigbook_manager /path/to/my/music
```

### `scripts/run_manager.py`
A standalone script that can be used from the `scripts/` directory.

## Supporting Files

### `igigbook_manager/manager.py`
Contains the `organize_and_export` function, which is the heart of the tool. It handles:
1. Iterating through all files in a source directory.
2. Cleaning up junk files.
3. Classifying files into category subdirectories (e.g., `Active`, `Books`, `Classical`).
4. Creating a `sync` folder for iGigbook.
5. Exporting a `library_index.csv`.

### `igigbook_manager/categories.py`
Defines the `PREFIX_MAP`, which dictates how files starting with certain codes are categorized.

### `igigbook_manager/utils.py`
Contains utility functions for:
- `classify_name`: Logic for mapping a file's prefix to a category.
- `is_booklist_name`: Detection for short, cryptic filenames (often used for indices).
- `normalize_name`: Renaming rules (e.g., swapping `!` for `_`).
