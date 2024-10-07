from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter Book Title: ")
    while True:
        authors = input("Enter multiple authors name by using semicolon (;): ")
        if ',' in authors:
            print("Can't use comma. Please use semecolon(;)")
        else:
            break

    isbn = input("Enter ISBN number: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }

    all_books.append(book)
    save_all_books(all_books)

    return all_books