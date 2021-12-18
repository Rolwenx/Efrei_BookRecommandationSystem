import utility_functions as utility
import recommandation_functions as recommendationfunctions
from books_functions import *

''' Function that will check if the string entered by the user is in the right format in the books read function : 
number,number,number'''


def check_if_string_is_good(string, list):
    for character in string:
        if character not in list:
            return False
    return True


'''def check_if_rank_entered_exist_in_depository(books_read_list):
    books_read_list = books_read_list.split(',')
    books_file = open("books.txt", 'r')
    books_list = utils.remove_gap(books_file.readlines())
    for character in range(len(books_read_list)):
        books_read_list[character] = int(books_read_list[character])
        for i in range(1,len(books_list)):
            if books_read_list[character] != i:
                del books_read_list[character]
    books_read_list = books_read_list.join(",")
    return books_read_list'''

# Function that will ask the user to enter the books that he has read and returns it as a string; ex : 15,2,23
def book_read_reader_profile():
    # List of the allowed values that the user is allowed to choose when entering his books read
    list_allowed_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
    print("\n" + "Among the following books, which ones have you read ?")
    list_books()
    books_read_list = input("Enter the numbers corresponding to the books (separated by commas. Ex : 1,2,4)\n> ")
    while not check_if_string_is_good(books_read_list, list_allowed_value):
        print("You didn't respect the wanted format of answer or entered a letter.")
        books_read_list = input("Enter the numbers in the correct format (separated by commas. Ex : 1,2,4)\n> ")
        check_if_string_is_good(books_read_list, list_allowed_value)
    # Now we check if the number entered by the user really exist in the depository
    return books_read_list


'''Global function that will check if a user exists in the readers.txt file plus return its position in the list if user
exist, or will return False if user doesn't exist'''
def check_if_user_already_exist_and_returns_rank(pseudo):
    with open("readers.txt", "r") as readers_list_checkers:
        readers_in_list = readers_list_checkers.readlines()
        for user in range(len(readers_in_list)):
            user_split = readers_in_list[user].split(",")
            if user_split[0] == pseudo:
                # The rank will return a value in the way of a list ("1" if the reader is the second, 0 if he's first..)
                rank = user
                return rank
    return False


'''Function that regroups others functions that aims to ask the users about his personal information so that his profile 
can be added in the database, therefore in the readers.txt'''


def add_reader_profile():
    readers_file_append = open("readers.txt", "a")
    file_books_read = open("booksread.txt", "a")
    reader_pseudo = utils.ask_user_pseudonym()
    does_reader_exist = check_if_user_already_exist_and_returns_rank(reader_pseudo)
    if not does_reader_exist:
        reader_gender = utils.ask_user_gender()
        reader_age = utils.ask_user_age()
        reader_age_category = utils.user_age_category_number(reader_age)
        reader_book_style = utils.ask_user_book_type()
        enter_books_read = book_read_reader_profile()
        readers_file_append.write(str(reader_pseudo) + str(","))
        file_books_read.write(str(reader_pseudo) + str(",") + str(enter_books_read) + str("\n"))
        readers_file_append.write(str(reader_gender) + str(",") + str(reader_age_category) + str(","))
        readers_file_append.write(str(reader_book_style) + str("\n"))
        # We now add a row in the scoring matrix file for the rating
        with open("books.txt", "r") as books_file:
            nbCol = len(books_file.readlines())
            new_reader_list = ['0'] * nbCol
            new_reader_list = " ".join(new_reader_list)
        with open("scoring_matrix.txt", "a") as scoring_matrix:
            scoring_matrix.write(str(new_reader_list) + str("\n"))
    else:
        print("This user already exist.")
    file_books_read.close()
    readers_file_append.close()


# Function that will delete a user
def delete_member():
    print("Which member do you want to delete?")
    member_to_delete = input("Enter their pseudonym : ")
    readers_list = open("readers.txt", "r")
    books_read_list = open("booksread.txt", "r")
    # We transform lines of readers.txt and booksread.txt into a list
    readers_lines = readers_list.readlines()
    books_read_lines = books_read_list.readlines()
    # We store the
    does_reader_exist = check_if_user_already_exist_and_returns_rank(member_to_delete)
    if not does_reader_exist:
        print("Member not found in our database.")
    else:
        readers_list = open("readers.txt", "w")
        books_read_list = open("booksread.txt", "w")
        # We overwrite the whole readers.txt file and write only the lines in which the user to delete isn't
        for line in readers_lines:
            if member_to_delete not in line:
                readers_list.write(line)
        # We overwrite the whole booksread.txt file and write only the lines in which the user to delete isn't
        for line2 in books_read_lines:
            if member_to_delete not in line2:
                books_read_list.write(line2)
        print("Member successfully deleted.")
        # We now delete the row corresponding to that user in the scoring matrix file for the rating system
        with open("scoring_matrix.txt") as scoring_matrix :
            # We store the file scoring matrix as a list where 1 item of list = 1 line of file
            scoring_matrix_rows = utility.remove_gap(scoring_matrix.readlines())
            # Since we stored the rank of the user that we want to delete in "does_reader_exist", we delete the
            # line attributed to that rank, to delete the user in the scoring matrix file
            del scoring_matrix_rows[does_reader_exist]
            # We write the new scoring matrix, without the line deleted in the scoring matrix file
            recommendationfunctions.write_in_scoring_matrix(scoring_matrix_rows)
    readers_list.close()
    books_read_list.close()


"""Function that will allow the user to view the numbers in the readers.txt file as a string. The format will return
items that are in different dictionaries initialized in the utility_functions file. We use the utils. since we 
imported the functions in the utility_functions as utils."""


def view_reader_profile():
    with open("readers.txt", "r") as readers_list, open("booksread.txt", "r") as booksread_list:
        list_of_all_readers = readers_list.readlines()
        list_of_booksread_lines = booksread_list.readlines()
        user_to_view = input("Which user do you want to view ?\n> ")
        does_reader_exist = check_if_user_already_exist_and_returns_rank(user_to_view)
        if not does_reader_exist:
            print("The member that you searched doesn't exist in our database.")
        else:
            # VIEW USER INFO IN READERS.TXT
            for user_info in list_of_all_readers:
                user_info_split = user_info.split(",")
                if user_info_split[0] == user_to_view:
                    print("NAME : {}".format(user_to_view))
                    print("GENDER : {}".format(utils.READER_GENDERS[int(user_info_split[1])]))
                    print("AGE RANGE : {}".format(utils.READER_AGES[int(user_info_split[2])]))
                    print("FAVOURITE TYPE OF BOOK : {}".format(utils.BOOK_GENRES[int(user_info_split[3])]))
            # VIEW USER INFO IN BOOKS_READ.TXT
            print("This user has read the following book :")
            for user_info_in_booksread in range(len(list_of_booksread_lines)):
                user_info_split = list_of_booksread_lines[user_info_in_booksread].split(",")
                if user_info_split[0] == user_to_view:
                    for i in range(1, len(user_info_split)):
                        books_list = open("books.txt", "r")
                        # We remove the \n in the list from the readlines() command
                        list_of_books = remove_jump_of_line_in_list(books_list.readlines())
                        # we initialized number_assigned_to_deleted_book to create the while loop
                        found_book, position_of_book = False, 0
                        while found_book == False and position_of_book < len(list_of_books):
                            if int(user_info_split[i]) == position_of_book:
                                print("- ", list_of_books[position_of_book])
                                found_book = True
                            position_of_book += 1


def edit_reader_profile():
    readers_list = open("readers.txt", "r")
    booksread_list = open("booksread.txt", "r")
    list_of_all_readers = readers_list.readlines()
    list_of_booksread_users = booksread_list.readlines()
    user_to_edit = input("Which user profile do you want to edit ?\n> ")
    does_reader_exist = check_if_user_already_exist_and_returns_rank(user_to_edit)
    if not does_reader_exist:
        print("The member that you searched doesn't exist in our database.")
    else:
        # EDIT USER INFO IN READERS LIST
        for user_info in list_of_all_readers:
            user_info_split = user_info.split(",")
            if user_info_split[0] == user_to_edit:
                parameter_to_edit = utils.FORBIDDEN_VALUE
                while parameter_to_edit <= 0 or parameter_to_edit > 5:
                    print("""Which parameter do you want to edit in that user's profile ? 
                                        1. Pseudonym
                                        2. Gender
                                        3. Age
                                        4. Book Type
                                        5. Book Read """)
                    parameter_to_edit = int(input("Enter the corresponding number : "))
                if parameter_to_edit == 1:
                    pseudonym = utils.ask_user_pseudonym()
                    user_info_split[0] = pseudonym
                    print(user_to_edit, "'s pseudonym has been modified to : ", pseudonym)
                elif parameter_to_edit == 2:
                    reader_gender = utils.ask_user_gender()
                    reader_gender = str(reader_gender)
                    user_info_split[1] = reader_gender
                    print(user_to_edit, 's gender is now : {}'.format(utils.READER_GENDERS[int(user_info_split[1])]))
                elif parameter_to_edit == 3:
                    reader_age = utils.ask_user_age()
                    reader_age_category = utils.user_age_category_number(reader_age)
                    reader_age_category = str(reader_age_category)
                    user_info_split[2] = reader_age_category
                    print(user_to_edit,
                          'is now in the following age range : {}'.format(utils.READER_AGES[int(user_info_split[2])]))
                elif parameter_to_edit == 4:
                    reader_book_style = utils.ask_user_book_type()
                    reader_book_style = str(reader_book_style)
                    user_info_split[3] = reader_book_style
                    print(user_to_edit,
                          'now likes the following type of book: {}'.format(utils.BOOK_GENRES[int(user_info_split[3])]))
                else:
                    books_that_user_has_read = book_read_reader_profile()
                    books_that_user_has_read = str(books_that_user_has_read)
                    print(books_that_user_has_read)
                    for user in range(len(list_of_booksread_users)):
                        user_info_split = list_of_booksread_users[user].split(",")
                        if user_info_split[0] == user_to_edit:
                            element = str(user_to_edit) + str(",") + str(books_that_user_has_read) + str("\n")
                            print(element)
                            list_of_booksread_users[user] = element
                        readers_list.close()
                        # We overwrite the whole file to enter new modified infos in booksread.txt and readers.txt
                    booksread_list = open("booksread.txt", "w")
                    booksread_list.close()
                    # Adding all the rest of readers
                    booksread_list = open("booksread.txt", "a")
                    for user in range(len(list_of_booksread_users)):
                        booksread_list.write(list_of_booksread_users[user])
                    booksread_list.close()


def reader_profiles_menu():
    print("""You are currently are on the "Reader Profiles" page. What do you want to do ?
    1. Display books
    2. Add a reader
    3. View a reader
    4. Edit a reader
    5. Delete a reader
    6. Return to the the launch menu""")
    reader_profiles_menu_selection = input("Enter the corresponding choice : ")
    while reader_profiles_menu_selection != '1' and reader_profiles_menu_selection != '2' and reader_profiles_menu_selection != '3' and reader_profiles_menu_selection != '4' and reader_profiles_menu_selection != '5' and reader_profiles_menu_selection != '6':
        print("You selected a nonexistent choice, choose again please.")
        reader_profiles_menu_selection = input("Enter the corresponding choice : ")
    reader_profiles_menu_selection = int(reader_profiles_menu_selection)
    print("\n")
    if reader_profiles_menu_selection == 1:
        list_books()
        print("\n \n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 2:
        add_reader_profile()
        print("\n \n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 3:
        view_reader_profile()
        print("\n \n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 4:
        edit_reader_profile()
        print("\n \n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 5:
        delete_member()
        print("\n \n")
        reader_profiles_menu()
    else:
        utils.launching_menu()
