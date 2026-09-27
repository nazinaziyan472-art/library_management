import json


FILE_NAME = "book.json"


def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# 1. ADD BOOK
def add_book():
    print("\n===== ADD BOOK =====")

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    if book_id.isspace():
        print("not valid")
        return 
    books = load_books()

    for book in books:
        if book["book_id"] == book_id:
            print("Book ID already exists!")
            return

    new_book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(new_book)
    save_books(books)

    print("Book added successfully!")


# 2. VIEW ALL BOOKS
def view_books():
    books = load_books()

    print("\n===== ALL BOOKS =====")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        print("--------------------------")
        print("Book ID :", book["book_id"])
        print("Title   :", book["title"])
        print("Author  :", book["author"])

        if book["available"]:
            print("Status  : Available")
        else:
            print("Status  : Issued")

    print("--------------------------")


# 3. SEARCH BOOK
def search_book():
    search = input("\nEnter Book ID or Book Title: ")

    books = load_books()

    for book in books:
        if (book["book_id"].lower() == search.lower()
                or book["title"].lower() == search.lower()):

            print("\n===== BOOK FOUND =====")
            print("Book ID :", book["book_id"])
            print("Title   :", book["title"])
            print("Author  :", book["author"])

            if book["available"]:
                print("Status  : Available")
            else:
                print("Status  : Issued")

            return

    print("Book not found.")


# 4. CHECK AVAILABILITY
def check_availability():
    book_id = input("\nEnter Book ID: ")

    books = load_books()

    for book in books:
        if book["book_id"] == book_id:

            if book["available"]:
                print("Book is available.")
            else:
                print("Book is not available.")

            return

    print("Book not found.")


# 5. ISSUE BOOK
def issue_book():
    book_id = input("\nEnter Book ID to issue: ")

    books = load_books()

    for book in books:
        if book["book_id"] == book_id:

            if book["available"]:
                book["available"] = False
                save_books(books)

                print("Book issued successfully.")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


# 6. RETURN BOOK
def return_book():
    book_id = input("\nEnter Book ID to return: ")

    books = load_books()

    for book in books:
        if book["book_id"] == book_id:

            if not book["available"]:
                book["available"] = True
                save_books(books)

                print("Book returned successfully.")
            else:
                print("Book is already available.")

            return

    print("Book not found.")


# 7. DELETE BOOK
def delete_book():
    book_id = input("\nEnter Book ID to delete: ")

    books = load_books()

    for book in books:
        if book["book_id"] == book_id:

            books.remove(book)
            save_books(books)

            print("Book deleted successfully.")
            return

    print("Book not found.")