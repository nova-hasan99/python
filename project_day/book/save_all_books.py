
def save_all_books(all_books):
    with open("all_books.csv", "w") as fp:
        for book in all_books:
            index = f"{book['title']}, {book['authors']}, {book['isbn']}, {book['year']}, {book['quantity']},"
            fp.write(index)
