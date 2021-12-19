'''
---- BOOK RECOMMENDATION SYSTEM
---- AUTHOR : Yoke NGASSA
---- ROLE : Stores all the functionalities related to the management of the Book depository
        such as :
        - Add a book
        - Delete a book
        - Edit a book
        - Display books
    + the functions related to those functionalities
'''

import utility_functions as utility
import recommendation_functions as recomfunctions


def display_list_of_book():
    '''
    Prints the list of the books preceded by the sequential number.

    RETURNS:
        Nothing : It's just a function that serves as a functionality
        It does something elsewhere without returning anything
        It shows to the user the list of books in depository
    '''

    with open("books.txt", "r", encoding="utf-8") as books_file:
        for i, line in enumerate(books_file, 1):
            print(i, ') ', line, end='')


def get_book_index(book_to_search):
    '''
    Checks if a book exists in the books.txt file and returns its index if so
    PARAMETER:
        < book_to_search > (string) : Title of the  book we want to see if exists in depository

    RETURNS:
        < False > (boolean) : If book not in depository, it returns False
        < book > (integer) : Index of the book in the depository in list language:
            If Book is second in depository,then book = 1
    '''

    with open("books.txt", "r", encoding="utf-8") as books_file:
        list_of_all_books = books_file.readlines()
        list_of_all_books = utility.remove_gap(list_of_all_books)

        # We run through the lines of the book.txt (as list) and if the book that
        # we search is the same as in the depository, it returns.

        for book in range(len(list_of_all_books)):
            if list_of_all_books[book] == book_to_search:
                return book
        return False


def add_book_to_depository():
    '''
    Add a book to the depository in the books.txt file

    RETURNS:
        Nothing : It's just a function that serves as a functionality
        It does something elsewhere without returning anything
        It adds the book name at the end of the books.txt file
    '''

    book_to_add = input('Enter the title of the book that you want to add\n> ')

    # We check if the book exists or not, and if he does, we store its index.
    book_idx = get_book_index(book_to_add)

    with open("books.txt", "a", encoding="utf-8") as books_file:

        if not book_idx:

            books_file.write(str(book_to_add) + str("\n"))
            print('This book is not in the depository. It\'s now added.')

            # We now add a column in the scoring matrix file for the rating system
            with open("scoring_matrix.txt", "r", encoding="utf-8") as scoring_matrix:
                scoring_matrix_lines = utility.remove_gap(
                    scoring_matrix.readlines())

            with open("scoring_matrix.txt", "w", encoding="utf-8") as scoring_matrix:
                # We browse in the list containing the lines of the scoring matrix files.
                # 1 line = 1 item of list
                for row in scoring_matrix_lines:
                    # We add now add a 0 to each line, meaning that we add this book to
                    # all users of the database
                    row = row + str(" ") + str('0')
                    scoring_matrix.write(str(row) + str("\n"))

        else:
            print("This book is already in the depository.")


def edit_book_in_depository():
    '''
    Edit an existing book of the depository.

    RETURNS:
        Nothing: It's just a function that serves as a functionality
        It does something elsewhere without returning anything
        It edits a book's title in the books.txt file
    '''

    print("Which book do you want to edit ? (exact title please)")
    old_book_title = input("Enter the name of the book :\n> ")

    # We check through the global function if the book exist or not.
    book_exists = get_book_index(old_book_title)

    if not book_exists:
        print("This book is not in the depository. Can't edit a non-existent book.")
        return

    with open("books.txt", "r", encoding="utf-8") as books_file:
        list_of_books = utility.remove_gap(books_file.readlines())

    new_book_tile = input("Enter the new book name:  ")
    for i, book_title in enumerate(list_of_books):
        if old_book_title == book_title:

            # We attribute the new book title to the old
            # ONLY in the list : list_of_books

            list_of_books[i] = new_book_tile
            break

    # We now overwrite the books.txt file and re-write it with the new book
    # name that we changed in the list_of_books
    with open("books.txt", "w", encoding="utf-8") as books_file:
        for books in list_of_books:
            books_file.write(str(books) + str("\n"))
        print("Book depository modified.")


def delete_book_in_depository():
    print("Which book do you want to delete ? (exact title please)")
    book_title_to_delete = input("Enter the name of the book :\n> ")
    does_book_exist = get_book_index(book_title_to_delete)

    if not does_book_exist:
        print("This book is not in the depository. Can't delete a non-existent book.")

    else:

        # DELETE THE BOOK IN THE BOOKS FILE
        books_list = open("books.txt", "r",encoding='utf-8')
        # We remove the \n in the list from the readlines() command
        list_of_books = utility.remove_gap(books_list.readlines())
        # we initialized found_book_to_delete and number_assigned_to_deleted_book to create the while loop
        found_book_to_delete, number_assigned_to_deleted_book = False, 0
        while found_book_to_delete == False and number_assigned_to_deleted_book < len(list_of_books):
            if book_title_to_delete == list_of_books[number_assigned_to_deleted_book]:
                del list_of_books[number_assigned_to_deleted_book]
                # we save the position of the deleted book from the list of books in a temp and we add one because
                # a list start at 0 but in books.txt, the first book is at 1'''
                temp_number = number_assigned_to_deleted_book + 1
                found_book_to_delete = True
            number_assigned_to_deleted_book += 1

        # re-write books.txt without the deleted book
        with open("books.txt", "w",encoding='utf-8') as books_list:
            for books in list_of_books:
                books_list.write(str(books) + str("\n"))
            print("The selected book has been deleted.")

        # DELETE THE BOOK NUMBER FOR THE USER WHO READ THE DELETED BOOK
        books_read = open("booksread.txt", "r",encoding='utf-8')
        booksread_users = utility.remove_gap(books_read.readlines())
        for k in range(len(booksread_users)):
            user = booksread_users[k].split(',')
            j = 1
            while j < len(user):
                temp_number = str(temp_number)
                if user[j] == temp_number:
                    del user[j]
                j = j + 1
        # Since we deleted a book, the rank in the booksread need to change.
            for i in range(1,len(user)):
                user[i] = int(user[i])
                if user[i] > does_book_exist :
                    user[i] = user[i] - 1
                user[i] = str(user[i])
            for h in range(1,len(user)):
                user[h] = str(user[h])
            user = ",".join(user)
            booksread_users[i] = user
        books_read = open("booksread.txt", "w",encoding='utf-8')
        for user in booksread_users:
            books_read.write(str(user) + str("\n"))

        # We now delete the row corresponding to that user in the scoring matrix file for the rating system
        with open("scoring_matrix.txt","r",encoding='utf-8') as scoring_matrix:

            # We store the file scoring matrix as a list where 1 item of list = 1 line of file
            scoring_matrix_rows = utility.remove_gap(scoring_matrix.readlines())

            # Since we stored the rank of the book that we deleted in "does_book_exist", we delete, in each line, the
            # item that correspond to the book's rank, therefore deleting the book in all line, in all reader's row
            does_book_exist = int(does_book_exist)
            for reader in range(len(scoring_matrix_rows)):
                we_split_books_of_reader = scoring_matrix_rows[reader].split(" ")
                del we_split_books_of_reader[does_book_exist]
                scoring_matrix_rows[reader] = ' '.join(we_split_books_of_reader)
            # We write the new scoring matrix, without the line deleted in the scoring matrix file
            recomfunctions.write_in_scoring_matrix(scoring_matrix_rows)

#Nolwen,22,20,21,16,8