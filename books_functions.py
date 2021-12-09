# When doing the split, there's a \n that appears. This function will delete it
def remove_jump_of_line_in_list(list):
    for i in range(len(list)):
        list[i] = list[i][:-1]
    return list


def list_books():
    """Prints the list of the books preceded by the sequential number"""
    books_list = open("books.txt", "r")
    a = 1
    for line in books_list:
        print(a, ') ', line, end='')
        a += 1
    number_of_books = len(books_list.readlines())
    books_list.close()
    return number_of_books


# Global function that will check if a book exists in the books.txt file while returning its rank
def check_if_book_exist_then_returns_its_rank(book_to_search):
    with open("books.txt", "r") as books_list:
        list_of_all_books = books_list.readlines()
        list_of_all_books = remove_jump_of_line_in_list(list_of_all_books)
        for book in range(len(list_of_all_books)):
            if list_of_all_books[book] == book_to_search:
                rank = book + 1
                return True, rank


# Global function that will check if a book exists in the books.txt file
def check_if_book_exist(book_to_search):
    with open("books.txt", "r") as books_list:
        list_of_all_books = books_list.readlines()
        list_of_all_books = remove_jump_of_line_in_list(list_of_all_books)
        for book in range(len(list_of_all_books)):
            if list_of_all_books[book] == book_to_search:
                return True


def add_book_to_depository():
    book_to_add = input('Enter the title of the book that you want to add\n> ')
    does_book_exist = check_if_book_exist(book_to_add)
    with open("books.txt", "a") as books_list:
        if does_book_exist:
            print("This book is already in the depository.")
        else:
            print('This book is not in the depository. It\'s now added.')
            books_list.write(str(book_to_add) + str("\n"))


def edit_book_in_depository():
    print("Which book do you want to edit ? (exact title please)")
    old_book_title = input("Enter the name of the book :\n> ")
    does_book_exist = check_if_book_exist(old_book_title)
    if does_book_exist:
        books_list = open("books.txt", "r")
        list_of_books = remove_jump_of_line_in_list(books_list.readlines())
        new_book_tile = input("Enter the new book name : ")
        for book in range(len(list_of_books)):
            if old_book_title == list_of_books[book]:
                list_of_books[book] = new_book_tile
                books_list.close()
                with open("books.txt", "w") as books_list:
                    for books in list_of_books:
                        books_list.write(str(books) + str("\n"))
                    print("Book depository modified.")
    else:
        print("This book is not in the depository. Can't edit a non-existent book.")


#######################################
def delete_book_in_depository():
    print("Which book do you want to delete ? (exact title please)")
    book_title_to_delete = input("Enter the name of the book :\n> ")
    does_book_exist = check_if_book_exist(book_title_to_delete)
    if does_book_exist:
        # DELETE THE BOOK IN THE BOOKS FILE
        books_list = open("books.txt", "r")
        # We remove the \n in the list from the readlines() command
        list_of_books = remove_jump_of_line_in_list(books_list.readlines())
        # we initialized found_book_to_delete and number_assigned_to_deleted_book to create the while loop
        found_book_to_delete, number_assigned_to_deleted_book = False, 0
        while found_book_to_delete == False and number_assigned_to_deleted_book < len(list_of_books):
            if book_title_to_delete == list_of_books[number_assigned_to_deleted_book]:
                del list_of_books[number_assigned_to_deleted_book]
                # we save the position of the deleted book from the list of books in a temp and we add one because
                # a list start at 0 but in books.txt, the first book is at 1
                temp_number = number_assigned_to_deleted_book + 1
                found_book_to_delete = True
            number_assigned_to_deleted_book += 1
        # re-write books.txt without the deleted book
        with open("books.txt", "w") as books_list:
            for books in list_of_books:
                books_list.write(str(books) + str("\n"))
            print("The selected book has been deleted.")
        # DELETE THE BOOK NUMBER FOR THE USER WHO READ THE DELETED BOOK
        books_read = open("booksread.txt", "r")
        booksread_users = remove_jump_of_line_in_list(books_read.readlines())
        for i in range(len(booksread_users)):
            user = booksread_users[i].split(',')
            print(user)
            for j in range(len(user)):
                temp_number = str(temp_number)
                print(temp_number)
                print(user[j])
                if user[j] == temp_number:
                    del user[j]
            user = ",".join(user)
            booksread_users[i] = user
        books_read = open("booksread.txt", "w")
        for user in booksread_users:
            books_read.write(str(user) + str("\n"))
    else:
        print("This book is not in the depository. Can't delete a non-existent book.")


def book_depository_menu():
    print("""You are currently are on the "Visit the Book Depository" page. What do you want to do ?
    1. Display books
    2. Add a book
    3. Edit a book
    4. Delete a book
    5. Return to the launch menu""")
    book_depository_menu_selection = input("Enter the corresponding choice : ")
    while book_depository_menu_selection != '1' and book_depository_menu_selection != '2' and book_depository_menu_selection != '3' and book_depository_menu_selection != '4' and book_depository_menu_selection != '5':
        print("You selected a nonexistent choice, choose again please.")
        book_depository_menu_selection = input("Enter the corresponding choice : ")
    book_depository_menu_selection = int(book_depository_menu_selection)
    print("\n")
    if book_depository_menu_selection == 1:
        list_books()
        print("\n \n")
        book_depository_menu()
    elif book_depository_menu_selection == 2:
        add_book_to_depository()
        print("\n \n")
        book_depository_menu()
    elif book_depository_menu_selection == 3:
        edit_book_in_depository()
        print("\n \n")
        book_depository_menu()
    elif book_depository_menu_selection == 4:
        delete_book_in_depository()
        print("\n \n")
        book_depository_menu()
    else:
        launching_menu()
