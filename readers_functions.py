'''
---- BOOK RECOMMENDATION SYSTEM
---- AUTHOR : Yoke NGASSA
---- ROLE : Stores all the functionalities related to the management of the Readers
    profiles such as :
        - Add reader
        - Delete reader
        - Edit reader
        - View reader
        - Display books
    + the functions related to those functionalities
'''

from utility_functions import remove_gap, is_string_correct_format, more_than_1_char
import recommendation_functions as recomfunctions
import books_functions as booksfunctions
from constants import READER_GENDERS, READER_AGES, BOOK_GENRES


def input_pseudonym():
    '''
    Asks the user to enter their username

    RETURNS:
        < pseudonym > (string) ; User's pseudo
    '''
    pseudonym = input('Enter the pseudonym ?\n> ')

    # Since it's too long to enter a list of all the characters allowed, we introduced
    # a list a forbidden value and make it so that the while loop will always run when
    # there's an item of that list in the Input

    while len(pseudonym) == 0 or is_string_correct_format(pseudonym, [',']) == True:
        print("This pseudonym contains forbidden values.")
        pseudonym = input('Enter the pseudonym ?\n')
    return pseudonym


def input_gender():
    '''
    Asks the user for its gender between : MAN, WOMAN, NO MATTER WHAT.

    RETURNS:
        < gender_number > (integer) : integer between 1 and 3
    '''

    list_allowed_value = ['1', '2', '3']
    print("""Enter the gender?
               1. MAN
               2. WOMAN
               3. NO MATTER WHAT""")
    gender_number = input("Enter the corresponding number : ")

    #  We secure the input to avoid that the user enters anything else than a number from 1 to 3.
    while is_string_correct_format(gender_number, list_allowed_value) == False or more_than_1_char(gender_number) == True:
        print("You didn't respect the wanted format of answer.")
        gender_number = input("Enter the correct corresponding number : ")

    # We secure the Input so that the user can't enter nothing.
    while len(gender_number) == 0:
        print("You didn't enter anything. Please enter something.")
        gender_number = input("Enter the correct corresponding number: ")

    gender_number = int(gender_number)
    return gender_number


def input_age():
    '''
    Ask the user to enter his age
    RETURNS:
        < age_reader > (integer)
    '''

    list_allowed_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    age_reader = input("Enter the age :\n> ")

    #  We secure the input so that the user can't enter any other value except the ones in the list.
    while is_string_correct_format(age_reader, list_allowed_value) == False or len(age_reader) == 0:
        print("You didn't respect the wanted format of answer or entered nothing.")
        age_reader = input("Enter your age in the correct format: ")

    age_reader = int(age_reader)
    return age_reader


def get_age_category(age_reader):
    '''Function that returns a number according to the age entered by the user in the previous function
        PARAMETERS:
             < age_reader > (integer): Stores the age entered by reader (from previous function),
        RETURNS:
             < number > (integer) : according to the age entered by reader, it gives a number associated to an age
                                    category : 1. Less than 18 years old / 2.Between 18 and 25 years old /
                                               3.More than 25 years old
    '''

    if age_reader <= 18:
        return 1
    elif 18 < age_reader <= 25:
        return 2
    else:
        return 3


def input_book_type():
    '''Asks the user his favourite book_type
        RETURNS:
             < book_type > (integer) : an integer between 0 and 8 that correspond to
                                       the book style's number in the print'''

    list_allowed_value = ['1', '2', '3', '4', '5', '6', '7']
    print("""What is the reading style among those ? :
            1. Sci-fi
            2. Biography
            3. Horror
            4. Romance
            5. Fable
            6. History
            7. Comedy""")
    book_type = input("Enter the corresponding number: ")

    #  We secure the input to avoid that the user enters anything else than a number from 1 to 7.
    while is_string_correct_format(book_type, list_allowed_value) == False or more_than_1_char(book_type) == True:
        print("You didn't respect the wanted format of answer.")
        book_type = input("Enter the correct corresponding number: ")

    #  We secure the input to avoid that the user enters nothing
    while len(book_type) == 0:
        print("You didn't enter anything. Please enter something.")
        book_type = input("Enter the correct corresponding number: ")
    book_type = int(book_type)
    return book_type


def does_value_exist_among(value):
    '''Function that Checks if the books entered by the user in the ask_book_read Function,
        are in the list of books

        PARAMETERS:
             < value > (string): Stores a value so that we can check if it's between 1 and the
             number of books

        RETURNS:
             < condition > (boolean) : It will be the condition. True if the Number is in the
             range, False if not
    '''

    with open("books.txt", "r", encoding="utf-8") as books_file:
        size_books_list = len(remove_gap(books_file.readlines()))

    if len(value) == 1:
        if int(value) >= size_books_list or value < 1:
            return False
    else:
        val = value.split(',')
        for i in val:
            if int(i) >= size_books_list or int(i) < 1:
                return False
    return True


def ask_book_read():
    '''Ask the user to enter the books that he has read and returns it as a string. Ex : 15,2,23.
        RETURNS:
             < book_read_list > (string) : A string containing the books read by user, which will be added in the
                                           booksread.txt file.
    '''

    list_allowed_value = ['0', '1', '2', '3',
                          '4', '5', '6', '7', '8', '9', ',']
    print("\nAmong the following books, which ones have you read ? : \n")
    booksfunctions.display_list_of_book()
    print("\nIf you haven't read any from this list, don't enter anything.")
    print("Please, separate the numbers with commas. Ex : 1,2,3,4")
    books_read = input(
        "Enter the number associated to the book that you've read : ")
    while (not is_string_correct_format(books_read, list_allowed_value)) or (not does_value_exist_among(books_read)):
        if not is_string_correct_format(books_read, list_allowed_value):
            print("\nWrong format.")
            print(
                "Please, separate the numbers with commas and enter numbers and not letters. Ex : 1,2,3,4")
            books_read = input(
                "Enter the number associated to the book that you've read : ")
        else:
            print("\nYou entered a number that is not inside the list")
            print(
                "Please, separate the numbers with commas and enter numbers and not letters. Ex : 1,2,3,4")
            books_read = input(
                "Enter the number associated to the book that you've read : ")
    while len(books_read) == 0:
        print('''You can't have not read anything. If the books that you've read is not in the list,
        please go add that book. And then edit your profile later. Enter any book from this list meanwhile''')
        books_read = input("Enter the number associated to the book that you've read : ")

    return books_read


def get_user_index(pseudo):
    """
    Global function that will check if a user exists in the readers.txt file plus return its position in the list if user
    exist, or will return False if user doesn't exist.
    PARAMETERS:
        < pseudo > : String given corresponding to the name to look for.
    RETURNS :
        < False > : The function return the boolean False if the name isn't in readers file .
        < rank > : The function return a integer corresponding to the place of the pseudonym (pseudo) if the name
                   is in readers file .
    """

    with open("readers.txt", "r", encoding="UTF-8") as readers_list_checkers:
        readers_in_list = remove_gap(readers_list_checkers.readlines())
        for user in range(0, len(readers_in_list)):
            user_split = readers_in_list[user].split(",")
            if user_split[0] == pseudo:
                return user
        return 'False'


def add_reader_profile():
    '''
    Function that regroups others functions that aims to ask the users about his personal information so that his profile
    can be added in the database, therefore in the readers.txt

    RETURNS :
              < Nothing > : Since it's a just a functionality variable, it doesn't return anything, except adding the user
              information in the 'readers.txt' and 'booksread.txt' file.
    '''

    pseudo = input_pseudonym()

    # We check if the user exists or not, and if he does, we store its index.

    reader_idx = get_user_index(pseudo)

    if reader_idx == 'False':
        gender = input_gender()
        age = input_age()
        age_category = get_age_category(age)
        book_style = input_book_type()

        enter_books_read = ask_book_read()
        # We write every info that we asked to the user, in the readers.txt and booksread.txt file
        with open('readers.txt', 'a', encoding='UTF-8') as readers_file:
            readers_file.write(pseudo + ',' + str(gender) +
                               ',' + str(age_category) + ',' + str(book_style) + '\n')

        with open('booksread.txt', 'a', encoding='UTF-8') as booksread_file:
            booksread_file.write(pseudo + ',' + enter_books_read + '\n')

        # We now add a row in the scoring matrix file for the rating/recommendation system
        with open('books.txt', 'r', encoding='UTF-8') as books_file:
            nb_col = len(books_file.readlines())
            new_reader_list = ['0'] * nb_col
            new_reader_list = ' '.join(new_reader_list)

        with open('scoring_matrix.txt', 'a', encoding='UTF-8') as scoring_matrix:
            scoring_matrix.write(str(new_reader_list) + str('\n'))

    else:
        print('This user already exist.')


def delete_member():
    '''
    Function that aims to delete a user's profile, if it exists, in the readers.txt 
    and booksread.txt

    RETURNS :
        < Nothing > : Since it's a just a functionality variable, it doesn't 
        return anything, except adding the user information in the 'readers.txt' 
        and 'booksread.txt' file.
    '''

    print('Which member do you want to delete?')

    list_forbidden_value = [' ']
    member_to_delete = input('Which user do you want to delete ?\n> ')

    # Since it's too long to enter a list of all the characters allowed,
    # we introduced a list a forbidden value and make it so that the while loop
    # will always run when there's an item of that list in the Input

    while len(member_to_delete) == 0 or is_string_correct_format(member_to_delete, list_forbidden_value) == True:
        print('You didn\'t enter anything. Please enter something.')
        member_to_delete = input('Which user do you want to delete ?\n> ')

    readers_file = open('readers.txt', 'r', encoding='UTF-8')
    books_read_file = open('booksread.txt', 'r', encoding='UTF-8')
    # We transform lines of readers.txt and booksread.txt into a list
    readers_lines = readers_file.readlines()
    books_read_lines = books_read_file.readlines()

    # We check if the user exists or not, and if he does, we store its index.
    reader_idx = get_user_index(member_to_delete)

    if reader_idx == 'False' :
        print('Member not found in our database.')
        return

    # We overwrite the whole readers.txt file and write only the lines in
    # which the user to delete isn't
    with open('readers.txt', 'w', encoding='UTF-8') as readers_file:
        for line in readers_lines:
            if member_to_delete not in line:
                readers_file.write(line)

    # We overwrite the whole booksread.txt file and write only the lines
    # in which the user to delete isn't
    with open('booksread.txt', 'w', encoding='UTF-8') as booksread_file:
        for line in books_read_lines:
            if member_to_delete not in line:
                booksread_file.write(line)

    print("Member successfully deleted.")

    # We now delete the row corresponding to that user in the scoring matrix
    # file for the rating system
    with open("scoring_matrix.txt", "r", encoding="UTF-8") as scoring_matrix:

        # We store the file scoring matrix as a list where
        # 1 item of list = 1 line of file
        scoring_matrix_rows = remove_gap(
            scoring_matrix.readlines())

    # Since we stored the rank of the user that we want to delete in "reader_idx",
    # we delete theline attributed to that index, to delete the user in the
    # scoring matrix file

    del scoring_matrix_rows[reader_idx]

    # We write the new scoring matrix, without the line deleted in the scoring matrix file
    recomfunctions.write_in_scoring_matrix(scoring_matrix_rows)


def view_reader_profile():
    '''
    Function that will allow the user to view the numbers in the readers.txt file 
    as strings. The format will return items that are in different dictionaries 
    (imported as utility) initialized in the utility_functions file.

    RETURNS :
        < Nothing > : Since it's a just a functionality variable, it doesn't return
        anything, except printing in the console, the reader's profile informations 
        as a string (if the reader exist)
    '''

    with open("readers.txt", "r", encoding="UTF-8") as readers_list, open("booksread.txt", "r",
                                                                          encoding="UTF-8") as booksread_list:
        list_of_all_readers = readers_list.readlines()
        list_of_booksread_lines = booksread_list.readlines()

    user_to_view = input("Which user do you want to view ?\n> ")

    # Since it's too long to enter a list of all the characters allowed,
    # we introduced a list a forbidden value and make it so that the while
    # loop will always run when there's an item of that list in the Input.

    while len(user_to_view) == 0 or is_string_correct_format(user_to_view, [' ']) == True:
        print("You didn't enter anything. Please enter something.")
        user_to_view = input("Which user do you want to view ?\n> ")

    # We check if the user exists or not, and if he does, we store its index.
    reader_idx = get_user_index(user_to_view)

    if reader_idx == 'False':
        print("The member that you searched doesn't exist in our database.")
        return

    # VIEW USER INFO IN READERS.TXT

    # With the rank stored in the reader_idx, we can access the line of that user
    # in the list_of_all_readers. We then split that line into a list, to access
    # the values of the line separately.

    user_info_split = list_of_all_readers[reader_idx].split(",")

    # The readers.txt file is like this : "Pseudonym, number, number, number".
    # We access the information of this user, using the number, number1 as keys
    # to the dictionaries.

    print("NAME : " + user_to_view)
    print("GENDER : " + READER_GENDERS[int(user_info_split[1])])
    print("AGE RANGE : " + READER_AGES[int(user_info_split[2])])
    print("FAVOURITE TYPE OF BOOK : " +
          BOOK_GENRES[int(user_info_split[3])])

    # VIEW USER INFO IN BOOKS_READ.TXT

    print("This user has read the following book :")

    # Like done previously, with the reader_idx, we can access the line of that
    # user in the list_of_all_booksread_lines. We then split that line into a list,
    # to access the values of the line separately.

    user_info_split = list_of_booksread_lines[reader_idx].split(
        ",")

    # This loop will allow us to see, for each number attributed in booksread (for the reader that we want to
    # view), which book (as a string) it correspond to. '''

    for i in range(1, len(user_info_split)):
        with open("books.txt", "r", encoding="UTF-8") as books_list:
            # We remove the \n in the list from the readlines() command
            list_of_books = remove_gap(books_list.readlines())

        # We initialized number_assigned_to_deleted_book to create the while loop
        found_book, position_of_book = False, 0

        # The while loop stops when we found which book title is attributed to the current number that the for
        # loop is running
        while not found_book and position_of_book < len(list_of_books):
            if int(user_info_split[i]) == position_of_book:
                print("-", list_of_books[position_of_book])
                found_book = True
            position_of_book += 1


def edit_reader_profile():
    '''
    Function that will allow the user to edit the numbers in the readers.txt
    file for any user (if they exist).

    RETURNS:
        < Nothing > : Since it's a just a functionality variable, it doesn't
        return anything, except printing in the console, the reader's profile
        informations as a string (if the reader exist)
    '''

    with open("readers.txt", "r", encoding="UTF-8") as readers_file:
        list_of_all_readers = readers_file.readlines()

    with open("booksread.txt", "r", encoding="UTF-8") as booksread_file:
        list_of_booksread_users = booksread_file.readlines()

    user_to_edit = input("Which user do you want to edit ?\n> ")

    # Since it's too long to enter a list of all the characters allowed, we introduced a
    # list a forbidden value and make it so that the while loop will always run when
    # there's an item of that list in the Input.

    while len(user_to_edit) == 0 or is_string_correct_format(user_to_edit, [' ']) == True:
        print("You didn't enter anything. Please enter something.")
        user_to_edit = input("Which user do you want to edit ?\n> ")

    # We check if the user exists or not, and if he does, we store his rank in the database
    does_reader_exist = get_user_index(user_to_edit)

    if does_reader_exist == 'False' :
        print("The member that you searched doesn't exist in our database.")

    else:
        # EDIT USER INFO IN READERS LIST

        # With the rank stored in the reader_idx, we can access the line of that user in the
        # list_of_all_readers. We then split that line into a list, to access the values of the line separately.

        user_info_split = list_of_all_readers[does_reader_exist].split(",")
        list_allowed_value = ['1', '2', '3', '4', '5']
        print("""Which parameter do you want to edit in that user's profile ? 
                        1. Pseudonym
                        2. Gender
                        3. Age
                        4. Book Type
                        5. Book Read """)
        parameter_to_edit = input("Enter the corresponding number : ")

        #  We secure the input to avoid that the user enters anything else than a number from 1 to 5.
        while is_string_correct_format(parameter_to_edit, list_allowed_value) == False or more_than_1_char(parameter_to_edit) == True:
            print("You didn't respect the wanted format of answer.")
            parameter_to_edit = input("Enter the corresponding number : ")

        #  We secure the input to avoid that the user enters nothing.
        while len(parameter_to_edit) == 0:
            print("You didn't enter anything. Please enter something.")
            parameter_to_edit = input(
                "Enter the correct corresponding number: ")
            parameter_to_edit = int(parameter_to_edit)

        # According to what the user want to change, we run the functions of the 'Add reader' functionality and then
        # replace the existent information with the new (ONLY in the List_of_all_readers)

        if parameter_to_edit == 1:
            pseudonym = input_pseudonym()
            user_info_split[0] = pseudonym
            print(user_to_edit, "'s pseudonym has been modified to : ", pseudonym)

        elif parameter_to_edit == 2:
            reader_gender = input_gender()
            reader_gender = str(reader_gender)
            user_info_split[1] = reader_gender
            print(user_to_edit, 's gender is now : {}'.format(
                READER_GENDERS[int(user_info_split[1])]))

        elif parameter_to_edit == 3:
            reader_age = input_age()
            reader_age_category = get_age_category(reader_age)
            reader_age_category = str(reader_age_category)
            user_info_split[2] = reader_age_category
            print(user_to_edit, 'is now in the following age range : {}'.format(
                READER_AGES[int(user_info_split[2])]))

        elif parameter_to_edit == 4:
            reader_book_style = input_book_type()
            reader_book_style = str(reader_book_style)
            user_info_split[3] = reader_book_style
            print(user_to_edit, 'now likes the following type of book: {}'.format(
                BOOK_GENRES[int(user_info_split[3])]))

        else:
            books_that_user_has_read = ask_book_read()
            books_that_user_has_read = str(books_that_user_has_read)

            # Thanks to the does_reader_exist, we have the rank of the user that
            # we want to edit the profile and we can replace the old line by a
            # new one, with the new values entered by the user

            list_of_booksread_users[does_reader_exist] = str(
                user_to_edit) + "," + str(books_that_user_has_read) + "\n"
            readers_file.close()

            # We overwrite the whole file to enter new modified infos in booksread.txt and readers.txt

            booksread_list = open("booksread.txt", "w", encoding="UTF-8")
            booksread_list.close()
            # Adding all the rest of readers
            booksread_list = open("booksread.txt", "a", encoding="UTF-8")
            for user in range(len(list_of_booksread_users)):
                booksread_list.write(list_of_booksread_users[user])
                booksread_list.close()
