# V 2.1.0

import books_operations as bo

#--------------------- Main -----------------
while True :
    print("==============================================")
    print("Press A to add a book")
    print("Press L to list all books")
    print("Press F to find a book")
    print("Press D to delete a book")
    print("Press Q to quit application")
    print("==============================================")
    choice = input("Enter Your Choice : ").upper()
    print("==============================================")
    if   choice == 'A' :
        bo.add_book()
    elif choice == 'L' :
        bo.list_books()
    elif choice == 'F' :
        bo.find_book()
    elif choice == 'D' :
        bo.delete_book()
    elif choice == 'Q' :
        break
    else :
        print("Wrong choice !")
