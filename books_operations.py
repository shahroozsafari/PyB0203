
books=[]

def add_book():
    global books                # Optional Code
    book = {}
    book["title"] = input("Enter title of the book : ")
    book["author"] = input("Enter author of the book : ")
    book["pages"] = int(input("Enter number of pages : "))
    book["price"] = float(input("Enter price of the book : "))
    book["isbn"] = input("Enter ISBN of the book : ")
    books.append(book)

def list_books():
    for book in books :
        print(f"Title of book : {book['title']}")
        print(f"Author of book : {book['author']}")
        print(f"Number of Pages : {book['pages']}")
        print(f"price of book : {book['price']}")
        print(f"ISBN of book : {book['isbn']}")
        print("------------------------------------")

def find_book():
    isbn = input("Enter ISBN to find book : ")
    for book in books :
        if book["isbn"] == isbn :
            print(f"Title of book : {book['title']}")
            print(f"Author of book : {book['author']}")
            print(f"Number of Pages : {book['pages']}")
            print(f"price of book : {book['price']}")
            print(f"ISBN of book : {book['isbn']}")
            print("------------------------------------")
            break
    else :
        print("This book IS NOt in books database !")

def delete_book():
    isbn = input("Enter ISBN to delete book : ")
    for book in books :
        if book["isbn"] == isbn :
            books.remove(book)
            print("The book has been deleted successfully")
            break
    else :
        print("This book IS NOt in books database !")
