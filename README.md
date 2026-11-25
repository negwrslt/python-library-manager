# Python Library Manager (`mylibrary`)

A modular, object-oriented Library Management System and installable Python package with an interactive command-line interface (CLI) and JSON data persistence.

## Features
- **Book Management**: Add, remove, and list cataloged books with title and author details.
- **Search Capabilities**: Case-insensitive search across titles and authors.
- **Persistent Storage**: Automatically saves and reloads book records from `library.json`.
- **Packaging & Modularity**: Packaged as a clean, reusable Python library (`mylibrary`) with standard `setup.py` and `pyproject.toml`.
- **Automated Testing**: Includes full unit tests using Python's `unittest` framework.

## Project Structure
```text
python-library-manager/
├── mylibrary/
│   ├── __init__.py      # Package export and version info
│   └── library.py       # Core Book and Library classes
├── tests/
│   ├── __init__.py
│   └── test_library.py  # Unit tests for the catalog operations
├── main.py              # Interactive CLI application
├── pyproject.toml       # Modern build configuration (PEP 517/518)
├── setup.py             # Packaging setup script
├── .gitignore           # Ignores build artifacts and runtime storage
└── README.md
```

## Quick Start

### 1. Run the Interactive CLI Directly
```bash
python main.py
```

### 2. Install as a Local Editable Package
You can install `mylibrary` into your active Python environment:
```bash
pip install -e .
```
After installation, the package can be imported in any Python script:
```python
from mylibrary import Library

lib = Library(storage_file="my_books.json")
lib.add_book("Fluent Python", "Luciano Ramalho")
print(lib.search_book("Python"))
```

### 3. Run Unit Tests
```bash
python -m unittest discover tests
```
