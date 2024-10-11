import add_book
import delete_book
import view_all_books

all_books = []

print("Welcome to Book Safari!")

menu_text = """
    Plase select an option:
    0. Exit
    1. Add Book
    2. View All Book
    3. Delet Book
"""
while True:
    print(menu_text)
    menu = input("Provide a number (0-3): ")
    if menu == "0":
        break
    elif menu == "1":
        all_books = add_book.add_books(all_books)
    # elif menu == 2:
    #     view_all_books.view_all_books(all_books)
    # elif menu == 3:
    #     all_books = delete_book.delete_book(all_books)
    else:
        print("Invalid Input")
