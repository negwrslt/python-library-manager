"""
Unit tests for the mylibrary package.
"""

import os
import unittest
from mylibrary.library import Book, Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_library.json"
        self.lib = Library(storage_file=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_book_creation_and_repr(self):
        book = Book("1984", "George Orwell")
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(str(book), "'1984' by George Orwell")
        self.assertEqual(book.to_dict(), {"title": "1984", "author": "George Orwell"})

    def test_add_book_success(self):
        success = self.lib.add_book("Clean Code", "Robert C. Martin")
        self.assertTrue(success)
        self.assertEqual(len(self.lib.books), 1)
        self.assertEqual(self.lib.books[0].title, "Clean Code")

    def test_add_book_empty_input_rejected(self):
        self.assertFalse(self.lib.add_book("", "Author"))
        self.assertFalse(self.lib.add_book("Title", "   "))
        self.assertEqual(len(self.lib.books), 0)

    def test_remove_book(self):
        self.lib.add_book("The Hobbit", "J.R.R. Tolkien")
        self.lib.add_book("Brave New World", "Aldous Huxley")

        # Case-insensitive removal
        self.assertTrue(self.lib.remove_book("the hobbit"))
        self.assertEqual(len(self.lib.books), 1)
        self.assertEqual(self.lib.books[0].title, "Brave New World")

        # Removing non-existent book
        self.assertFalse(self.lib.remove_book("Unknown Book"))
        self.assertEqual(len(self.lib.books), 1)

    def test_search_book(self):
        self.lib.add_book("Python Crash Course", "Eric Matthes")
        self.lib.add_book("Fluent Python", "Luciano Ramalho")
        self.lib.add_book("Design Patterns", "Erich Gamma")

        # Search by title
        results = self.lib.search_book("Python")
        self.assertEqual(len(results), 2)

        # Search by author
        results_author = self.lib.search_book("Ramalho")
        self.assertEqual(len(results_author), 1)

        # Search query not found
        results_none = self.lib.search_book("Nonexistent")
        self.assertEqual(results_none, [])

    def test_persistence(self):
        self.lib.add_book("Dune", "Frank Herbert")

        # Create a new Library instance pointing to the same file
        reloaded_lib = Library(storage_file=self.test_file)
        self.assertEqual(len(reloaded_lib.books), 1)
        self.assertEqual(reloaded_lib.books[0].title, "Dune")
        self.assertEqual(reloaded_lib.books[0].author, "Frank Herbert")


if __name__ == "__main__":
    unittest.main()
