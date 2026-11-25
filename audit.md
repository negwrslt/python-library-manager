# Technical Audit & Backlog: Python Library Manager (`mylibrary`)

## 1. Original Technical Issues Identified
During code review and static analysis of the initial implementation (`تمرین22`), the following architectural defects and edge cases were identified:

| ID | Issue Description | Severity | Status |
| :--- | :--- | :--- | :--- |
| **ARCH-01** | **Lack of Data Persistence**: Book records were stored purely in an in-memory Python list. All records vanished upon program termination. | High | Fixed (added JSON auto-persistence) |
| **ARCH-02** | **String-Based Data Representation**: Books were formatted directly as raw strings (`f"'{title}' by {author}"`). Substring removal matching on `title in book` could accidentally match the author or wrong titles. | High | Fixed (introduced dedicated `Book` class) |
| **BUG-01** | **Case Sensitivity Issues**: `remove_book` and `search_book` failed to locate items if the letter casing didn't match exactly. | Medium | Fixed (case-insensitive normalized matching) |
| **BUG-02** | **Unvalidated Empty Inputs**: Empty strings for title and author were allowed, creating phantom book records. | Medium | Fixed (empty input validation added) |
| **PKG-01** | **Incomplete Packaging**: `setup.py` lacked modern standard build configurations (PEP 517/518), package metadata, description, and console script entrypoints. | Medium | Fixed (configured `setup.py` & `pyproject.toml`) |

---

## 2. Technical Debt & Backlog (To-Do Later)
Features, architecture upgrades, and technical debt earmarked for future sprints:

- [ ] **ISBN & Metadata Expansion**: Extend the `Book` model with `isbn` (validation with 10/13 digits), `year`, `genre`, and `copies_count`.
- [ ] **Borrow & Return System**: Add member/user profiles and a borrowing tracker (`borrower_name`, `borrow_date`, `due_date`, `is_returned`).
- [ ] **Sorting Capabilities**: Add sorting options to `show_books()` (by title, author, or date added).
- [ ] **Database Backend Support**: Implement an abstract storage interface with pluggable backends (e.g. SQLite via `sqlite3` alongside JSON).
- [ ] **Interactive CLI Testing**: Add automated integration tests using `unittest.mock.patch` to simulate interactive CLI menu sessions.
- [ ] **Export Formats**: Add support to export book catalog to CSV or Markdown table.
