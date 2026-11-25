"""
Main interactive entry point for the Library Management System.
"""

from mylibrary.library import Library


def menu():
    lib = Library(storage_file="library.json")

    while True:
        print("\n" + "=" * 25)
        print("    Library Menu")
        print("=" * 25)
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input("\nChoose an Option (1-5): ").strip()

        if choice == "1":
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            lib.add_book(title, author)

        elif choice == "2":
            title = input("Title of the book to remove: ").strip()
            lib.remove_book(title)

        elif choice == "3":
            query = input("Title or author to search: ").strip()
            results = lib.search_book(query)
            if results:
                print("\nMatching Books:")
                for r in results:
                    print(f" - {r}")

        elif choice == "4":
            print("\nCurrent Library Catalog:")
            books = lib.show_books()
            if books:
                for idx, book in enumerate(books, 1):
                    print(f"{idx}. {book}")

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    menu()
