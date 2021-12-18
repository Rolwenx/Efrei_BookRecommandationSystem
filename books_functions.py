# --------------------- MANAGING BOOK DEPOSITORY FUNCTIONS RELATED -----------------
import utility_functions as utility

# When doing the split, there's a \n that appears. This function will delete it and return the list without it.
def remove_jump_of_line_in_list(list):
    for i in range(len(list)):
        list[i] = list[i][:-1]
    return list


# This function is going to display the books in the depository with a number attributed to it according to its position
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


'''Global function that will check if a book exists in the books.txt file. If the book exist, it returns the book rank
but if it doesn't exist, it returns false'''


def check_if_book_exist_then_returns_its_rank(book_to_search):
    with open("books.txt", "r") as books_list:
        list_of_all_books = books_list.readlines()
        list_of_all_books = utility.remove_gap(list_of_all_books)
        for book in range(len(list_of_all_books)):
            if list_of_all_books[book] == book_to_search:
                return book
        return False


# Global function that will check if a book exists in the books.txt file and returns True.
def check_if_book_exist(book_to_search):
    with open("books.txt", "r") as books_list:
        list_of_all_books = books_list.readlines()
        list_of_all_books = utility.remove_gap(list_of_all_books)
        for book in range(len(list_of_all_books)):
            if list_of_all_books[book] == book_to_search:
                return True


'''Global function that will add a book to the depository. It doesn't return anything but it adds the book name in the 
books.txt file'''


def add_book_to_depository():
    book_to_add = input('Enter the title of the book that you want to add\n> ')
    does_book_exist = check_if_book_exist(book_to_add)
    with open("books.txt", "a") as books_list:
        if does_book_exist:
            print("This book is already in the depository.")
        else:
            print('This book is not in the depository. It\'s now added.')
            books_list.write(str(book_to_add) + str("\n"))
            # We now add a column in the scoring matrix file for the rating system
            with open("scoring_matrix.txt", "r") as scoring_matrix:
                scoring_matrix_lines = utility.remove_gap(scoring_matrix.readlines())
                scoring_matrix = open("scoring_matrix.txt", "w")
            # We browse in the list containing the lines of the scoring matrix files. 1 line = 1 item of list
            for row in scoring_matrix_lines :
                # We add now add a 0 to each line, meaning that we add this book to all users of the database
                row = row + str(" ")+str('0')
                scoring_matrix.write(str(row)+str("\n"))
            scoring_matrix.close()


'''Global function that will edit a book to the depository. It doesn't return anything but it edit the book name in the 
books.txt file'''


def edit_book_in_depository():
    print("Which book do you want to edit ? (exact title please)")
    old_book_title = input("Enter the name of the book :\n> ")
    # We check through the global function if the book exist or not.
    does_book_exist = check_if_book_exist(old_book_title)
    if does_book_exist:
        books_list = open("books.txt", "r")
        list_of_books = remove_jump_of_line_in_list(books_list.readlines())
        new_book_tile = input("Enter the new book name : ")
        for book in range(len(list_of_books)):
            if old_book_title == list_of_books[book]:
                # we attribute the new book title to the old ONLY in the list : list_of_books
                list_of_books[book] = new_book_tile
                books_list.close()
                # We overwrite the books.txt file and re-write it with the new book name that we changed in the
                # list_of_books
                with open("books.txt", "w") as books_list:
                    for books in list_of_books:
                        books_list.write(str(books) + str("\n"))
                    print("Book depository modified.")
    else:
        print("This book is not in the depository. Can't edit a non-existent book.")


''' Function that aims to first delete a book in the book depository (if it exists) and then delete the number
associated to that book in the booksread.txt file. The function doesn't return anything but it does modify the books.txt
and booksread.txt files.'''


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
                '''we save the position of the deleted book from the list of books in a temp and we add one because
                a list start at 0 but in books.txt, the first book is at 1'''
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
        booksread_users = books_read.readlines()
        # Loop that removes the /n in the readlines list but it displays the list like so : ['item','','item2','',
        # 'item3']
        for i in range(len(booksread_users)):
            booksread_users[i - 1] = booksread_users[i - 1][:-1]
        # With this loop, it will remove the additional '' in the previous lists
        for i in range(len(booksread_users)):
            if booksread_users[i] == '':
                del booksread_users[i]
        for i in range(len(booksread_users)):
            user = booksread_users[i].split(',')
            j = 0
            while j < len(user):
                temp_number = str(temp_number)
                if user[j] == temp_number:
                    del user[j]
                j = j + 1
            user = ",".join(user)
            booksread_users[i] = user
        books_read = open("booksread.txt", "w")
        for user in booksread_users:
            books_read.write(str(user) + str("\n"))
    else:
        print("This book is not in the depository. Can't delete a non-existent book.")


# Function that allows the user to browse the "Managing book depository" and apply its functionalities.
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
