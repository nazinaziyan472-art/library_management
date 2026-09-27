from user import user
import book


# USER SIGNUP
user1 = user()
user1.signup()


# MAIN MENU
while True:

    print("\n=============================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Check Availability")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Delete Book")
    print("8. Exit")
    print("==============================")

    choice = input("Enter your choice: ")


    # ADD BOOK
    if choice == "1":
        book.add_book()

    # VIEW ALL BOOKS
    elif choice == "2":
        book.view_books()


    # SEARCH BOOK
    elif choice == "3":
        book.search_book()


    # CHECK AVAILABILITY
    elif choice == "4":
        book.check_availability()


    # ISSUE BOOK
    elif choice == "5":
        book.issue_book()


    # RETURN BOOK
    elif choice == "6":
        book.return_book()


    # DELETE BOOK
    elif choice == "7":
        book.delete_book()


    # EXIT
    elif choice == "8":
        print("Thank you!")
        break


    else:
        print("Invalid choice. Please enter 1 to 8.")