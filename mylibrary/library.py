"""
Library Management Module
Defines the Book and Library classes for cataloging, searching, and managing books.
"""

import json
import os
from typing import List, Optional


class Book:
    """
    Represents an individual book in the library catalog.
    """
    def __init__(self, title: str, author: str):
        self.title = title.strip()
        self.author = author.strip()

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title.lower() == other.title.lower() and self.author.lower() == other.author.lower()

    def to_dict(self) -> dict:
        return {"title": self.title, "author": self.author}

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(title=data.get("title", ""), author=data.get("author", ""))


class Library:
    """
    Manages a collection of books with support for adding, removing,
    searching, and persistent JSON storage.
    """
    def __init__(self, storage_file: Optional[str] = "library.json"):
        self.storage_file = storage_file
        self.books: List[Book] = []
        if self.storage_file:
            self.load_from_file()

    def add_book(self, title: str, author: str) -> bool:
        """
        Adds a new book to the library catalog.
        Returns True if successful, False if input was empty.
        """
        clean_title = title.strip()
        clean_author = author.strip()

        if not clean_title or not clean_author:
            print("Error: Both title and author are required.")
            return False

        new_book = Book(clean_title, clean_author)
        self.books.append(new_book)
        print("Book added successfully!")
        self.save_to_file()
        return True

    def remove_book(self, title: str) -> bool:
        """
        Removes a book matching the given title (case-insensitive).
        Returns True if removed, False otherwise.
        """
        target = title.strip().lower()
        if not target:
            print("Error: Please provide a book title to remove.")
            return False

        for book in self.books:
            if target == book.title.lower() or target in book.title.lower():
                self.books.remove(book)
                print(f"The book '{book.title}' has been removed!")
                self.save_to_file()
                return True

        print("Book not found!")
        return False

    def search_book(self, query: str) -> List[str]:
        """
        Searches books by title or author substring (case-insensitive).
        Returns a list of formatted book strings for backwards-compatibility.
        """
        clean_query = query.strip().lower()
        if not clean_query:
            print("Error: Search query cannot be empty.")
            return []

        results = [
            str(book)
            for book in self.books
            if clean_query in book.title.lower() or clean_query in book.author.lower()
        ]

        if not results:
            print("No books found!")
        return results

    def show_books(self) -> List[str]:
        """
        Returns a list of all formatted book strings in the library.
        """
        if not self.books:
            print("No books available!")
            return []
        return [str(book) for book in self.books]

    def save_to_file(self) -> None:
        """Saves catalog to JSON file if storage_file is enabled."""
        if not self.storage_file:
            return
        try:
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump([b.to_dict() for b in self.books], f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"Warning: Failed to save library data: {e}")

    def load_from_file(self) -> None:
        """Loads catalog from JSON file if it exists."""
        if not self.storage_file or not os.path.exists(self.storage_file):
            return
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    self.books = [Book.from_dict(item) for item in data if isinstance(item, dict)]
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: Failed to read existing library data ({e}). Initialized empty library.")
