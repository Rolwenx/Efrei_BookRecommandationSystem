'''---- BOOK RECOMMENDATION SYSTEM
   ---- AUTHOR : Yoke NGASSA - Joseph Bénard
   ---- ROLE : Stores all the functionalities related to the management of the Readers profiles such as : Add reader
        delete reader, edit reader, view reader, display books + the functions related to those functionalities'''

import utility_functions as utility
import recommandation_functions as recommendationfunctions
from main_code import *
import books_functions as booksfunctions

'''Asks the user to enter their username
        PARAMETERS:

             < pseudonym > (string): Stores the pseudonym of user
             < list_forbidden_value > (list) : Store the forbidden values that can't be included in the user's pseudo
                                               Will be used to check if the pseudo is good in "check_if_string_is_good
             
        RETURNS:

              < pseudonym > (string) ; User's pseudo'''


def Input_Ask_Pseudonym():
    list_forbidden_value = [' ']
    pseudonym = input('Enter the pseudonym ? \n')
    while len(pseudonym) == 0 or utility.check_if_string_is_good(pseudonym, list_forbidden_value) == True:
        print("You didn't enter anything. Please enter something.")
        pseudonym = input('Enter the pseudonym ?\n')
    return pseudonym


'''Function that ask the user for its gender between : MAN, WOMAN, NO MATTER WHAT.
        PARAMETERS:

             < gender_number > (string): Stores the number associated to the gender of user
             < list_allowed_value > (list) : Store the only allowed values that the gender_number variable can have
                                               Will be used to check if the pseudo is good in "check_if_string_is_good
            < check_if_string_is_good > (function) : Check if the format entered by the user is correct
            < does_string_more_than_one_char > (function) : We only want a 1 character input, so this function checks it
             
        RETURNS:

             < gender_number > (integer) : integer between 1 and 3'''


def Input_Ask_Gender():
    list_allowed_value = ['1', '2', '3']
    print("""Enter the gender?
               1. MAN
               2. WOMAN 
               3. NO MATTER WHAT""")
    gender_number = input("Enter the corresponding number : ")
    while not utility.check_if_string_is_good(gender_number,
                                              list_allowed_value) or utility.does_string_more_than_one_char(
        gender_number) == True:
        print("You didn't respect the wanted format of answer.")
        gender_number = input("Enter the correct corresponding number : ")
    while len(gender_number) == 0:
        print("You didn't enter anything. Please enter something.")
        gender_number = input("Enter the correct corresponding number: ")
    gender_number = int(gender_number)
    return gender_number


'''Ask the user to enter his age
        PARAMETERS:

             < age_reader > (string): Stores the age entered by the user
             < list_allowed_value > (list) : Store the only allowed values that the age_reader variable can have
                                               Will be used to check if the pseudo is good in "check_if_string_is_good"

        RETURNS:

             < age_reader > (integer)'''


def Input_Ask_Age():
    list_allowed_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    age_reader = input("Enter the age :\n> ")
    while utility.check_if_string_is_good(age_reader, list_allowed_value) == False or len(age_reader) == 0:
        print("You didn't respect the wanted format of answer or entered nothing.")
        age_reader = input("Enter your age in the correct format: ")
    age_reader = int(age_reader)
    return age_reader


'''Function that returns a number according to the age entered by the user in the previous function
        PARAMETERS:

             < age_reader > (integer): Age entered by reader is stored in the variable (from previous function)

        RETURNS:

             < number > (integer) : according to the age entered by reader, it gives a number associated to an age 
                                    category : 1. Less than 18 years old / 2.Between 18 and 25 years old / 
                                               3.More than 25 years old'''


def Age_Category_Number(age_reader):
    if age_reader <= 18:
        return 1
    elif 18 < age_reader <= 25:
        return 2
    else:
        return 3


'''Ask the user his favourite book_type
        PARAMETERS:

             < book_type > (string): Stores the number associated to the favourite book type of user
             < list_allowed_value > (list) : Store the only allowed values that the age_reader variable can have
                                               Will be used to check if the pseudo is good in "check_if_string_is_good"

        RETURNS:

             < book_type > (integer) : an integer between 0 and 8 that correspond to
                                       the book style's number in the print'''


def Input_Book_Type():
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
    while utility.check_if_string_is_good(book_type,
                                          list_allowed_value) == False or utility.does_string_more_than_one_char(
        book_type) == True:
        print("You didn't respect the wanted format of answer.")
        book_type = input("Enter the correct corresponding number: ")
    while len(book_type) == 0:
        print("You didn't enter anything. Please enter something.")
        book_type = input("Enter the correct corresponding number: ")
    book_type = int(book_type)
    return book_type


'''Ask the user to enter the books that he has read and returns it as a string; ex : 15,2,23
        PARAMETERS:

             < book_read_list > (string): Stores the number associated to the books read by the user
             < list_allowed_value > (list) : Store the only allowed values that the book_read_list variable can have
                                               Will be used to check if the pseudo is good in "check_if_string_is_good"

        RETURNS:

             < book_read_list > (string) : A string containing the books read by user, which will be added in the
                                           booksread.txt file'''

def Is_String_Correct_Format(string, list):
    books_list = open("books.txt",'r')
    for character in string:
        if character not in list:
            return 'False'
    return 'True'

def Is_Input_Among_Book(value):
    books_file = open("books.txt","r")
    size_books_list = len(utility.remove_gap(books_file.readlines()))
    if 1 <= value <= size_books_list:
        return "True"
    return "False"



def Input_Ask_Book_Read():
    list_allowed_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
    print("\nAmong the following books, which ones have you read ? : \n")
    booksfunctions.Display_List_Of_Book()
    print("\nIf you haven't read any from this list, don't enter anything.")
    print("Please, separate the numbers with commas. Ex : 1,2,3,4")
    books_read = input("Enter the number associated to the book that you've read : ")
    if Is_String_Correct_Format(books_read, list_allowed_value) == 'False':
        print("\nWrong format.")
        print("Please, separate the numbers with commas and enter numbers and not letters. Ex : 1,2,3,4")
        books_read = input("Enter the number associated to the book that you've read : ")
    books_read = books_read.split(",")
    size_books_read = len(books_read)
    for i in range(0,size_books_read):
        books_read[i] = int(books_read[i])
        is_there_error_in_Input = Is_Input_Among_Book(books_read[i])
        if is_there_error_in_Input == 'False':
            del books_read[i]
            size_books_read = size_books_read - 1
        books_read[i] = str(books_read[i])
    books_read = ",".join(books_read)
    return books_read

'''Global function that will check if a user exists in the readers.txt file plus return its position in the list if user
exist, or will return False if user doesn't exist
PARAMETERS:

             readers_in_list (list): Stores the line of the reader.txt file as a list
             user_split (list) : Each item of the previous list is split in a sub-list to access elements of that line
             pseudo : Pseudonym of the user, defined in ask_user_pseudonym

RETURNS:

             < rank > (integer) : The number of the line that the user is in the readers.txt file. It's in list language.
                              Meaning that if the reader is on line 1, rank = 0
             < rank > (boolean) : False if the user doesn't exist in the readers.txt file'''


def Check_If_User_Exists_And_Return_Rank(pseudo):
    with open("readers.txt", "r", encoding="UTF-8") as readers_list_checkers:
        readers_in_list = utility.remove_gap(readers_list_checkers.readlines())
        for user in range(0,len(readers_in_list)):
            user_split = readers_in_list[user].split(",")
            if user_split[0] == pseudo:
                return user
        return "don't exist"


'''Function that regroups others functions that aims to ask the users about his personal information so that his profile 
can be added in the database, therefore in the readers.txt'''

'''PARAMETERS:
              < readers_file_append > (file) : Name given to the "readers.txt" file
              < file_books_read > (file) : Name given to the "booksread.txt" file
              < reader_pseudo > (string) : Stores the pseudo of the user
              < reader_gender > (integer) : Stores the gender of the user
              < reader_age > (integer) : Stores the age of the user
              < reader_age_category > (integer) : Stores the age category of the user
              < reader_book_style > (integer) : Store the favourite book style of the user
              < enter_books_read > (string) : Store a list of books read by the user
              < nbCol > (list) : Stores the lines in the books.txt file as a list
               
    RETURNS : 
              < Nothing > : Since it's a just a functionality variable, it doesn't return anything, except adding the user 
              information in the 'readers.txt' and 'booksread.txt' file.
'''


def add_reader_profile():
    readers_file_append = open("readers.txt", "a", encoding="UTF-8")
    file_books_read = open("booksread.txt", "a", encoding="UTF-8")
    reader_pseudo = Input_Ask_Pseudonym()
    does_reader_exist = Check_If_User_Exists_And_Return_Rank(reader_pseudo)
    if does_reader_exist == "don't exist":
        reader_gender = Input_Ask_Gender()
        reader_age = Input_Ask_Age()
        reader_age_category = Age_Category_Number(reader_age)
        reader_book_style = Input_Book_Type()
        enter_books_read = Input_Ask_Book_Read()
        # We write every info that we asked to the user, in the readers.txt and booksread.txt file
        readers_file_append.write(str(reader_pseudo) + str(","))
        file_books_read.write(str(reader_pseudo) + str(",") + str(enter_books_read) + str("\n"))
        readers_file_append.write(str(reader_gender) + str(",") + str(reader_age_category) + str(","))
        readers_file_append.write(str(reader_book_style) + str("\n"))
        # We now add a row in the scoring matrix file for the rating/recommendation system
        with open("books.txt", "r", encoding="UTF-8") as books_file:
            nbCol = len(books_file.readlines())
            new_reader_list = ['0'] * nbCol
            new_reader_list = " ".join(new_reader_list)
        with open("scoring_matrix.txt", "a", encoding="UTF-8") as scoring_matrix:
            scoring_matrix.write(str(new_reader_list) + str("\n"))
    else:
        print("This user already exist.")
    file_books_read.close()
    readers_file_append.close()


'''PARAMETERS:
              < readers_file_append > (file) : Name given to the "readers.txt" file
              < file_books_read > (file) : Name given to the "booksread.txt" file
              < reader_pseudo > (string) : Stores the pseudo of the user
              < reader_gender > (integer) : Stores the gender of the user
              < reader_age > (integer) : Stores the age of the user
              < reader_age_category > (integer) : Stores the age category of the user
              < reader_book_style > (integer) : Store the favourite book style of the user
              < enter_books_read > (string) : Store a list of books read by the user
              < nbCol > (list) : Stores the lines in the books.txt file as a list

    RETURNS : 
              < Nothing > : Since it's a just a functionality variable, it doesn't return anything, except adding the user 
              information in the 'readers.txt' and 'booksread.txt' file.
'''


def delete_member():
    print("Which member do you want to delete?")
    member_to_delete = input("Enter their pseudonym : ")
    readers_list = open("readers.txt", "r", encoding="UTF-8")
    books_read_list = open("booksread.txt", "r", encoding="UTF-8")
    # We transform lines of readers.txt and booksread.txt into a list
    readers_lines = readers_list.readlines()
    books_read_lines = books_read_list.readlines()
    # We store the
    does_reader_exist = Check_If_User_Exists_And_Return_Rank(member_to_delete)
    if not does_reader_exist:
        print("Member not found in our database.")
    else:
        readers_list = open("readers.txt", "w", encoding="UTF-8")
        books_read_list = open("booksread.txt", "w", encoding="UTF-8")
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
        with open("scoring_matrix.txt", "r", encoding="UTF-8") as scoring_matrix:
            # We store the file scoring matrix as a list where 1 item of list = 1 line of file
            scoring_matrix_rows = utility.remove_gap(scoring_matrix.readlines())
            # Since we stored the rank of the user that we want to delete in "does_reader_exist", we delete the
            # line attributed to that rank, to delete the user in the scoring matrix file
            del scoring_matrix_rows[does_reader_exist]
            # We write the new scoring matrix, without the line deleted in the scoring matrix file
            recommendationfunctions.Write_In_Scoring_Matrix(scoring_matrix_rows)
    readers_list.close()
    books_read_list.close()


'''Function that will allow the user to view the numbers in the readers.txt file as strings. The format will return
items that are in different dictionaries (imported as utility) initialized in the utility_functions file.'''

'''PARAMETERS:
              < readers_file_append > (file) : Name given to the "readers.txt" file
              < file_books_read > (file) : Name given to the "booksread.txt" file
              < reader_pseudo > (string) : Stores the pseudo of the user
              < reader_gender > (integer) : Stores the gender of the user
              < reader_age > (integer) : Stores the age of the user
              < reader_age_category > (integer) : Stores the age category of the user
              < reader_book_style > (integer) : Store the favourite book style of the user
              < enter_books_read > (string) : Store a list of books read by the user
              < nbCol > (list) : Stores the lines in the books.txt file as a list
               
    RETURNS : 
              < Nothing > : Since it's a just a functionality variable, it doesn't return anything, except printing in
              the console, the reader's profile informations as a string (if the reader exist)
              
'''


def view_reader_profile():
    with open("readers.txt", "r", encoding="UTF-8") as readers_list, open("booksread.txt", "r",
                                                                          encoding="UTF-8") as booksread_list:
        list_of_all_readers = readers_list.readlines()
        list_of_booksread_lines = booksread_list.readlines()
        user_to_view = input("Which user do you want to view ?\n> ")
        does_reader_exist = Check_If_User_Exists_And_Return_Rank(user_to_view)
        if does_reader_exist == "don't exist" :
            print("The member that you searched doesn't exist in our database.")
        else:
            # VIEW USER INFO IN READERS.TXT

            ''' The does_reader_exist returns the rank of the reader that we searched in the user_to_view only if the
            reader is in the database. Therefore, with his rank we can access the line of that user in the 
            list_of_all_readers. We then split that line into a list, to access the values of the line separately.'''
            user_info_split = list_of_all_readers[does_reader_exist].split(",")

            ''' The readers.txt file is like this : "Pseudonym, number, number1,number". We access
                the information of this user, using the number, number1 as keys to the dictionaries.'''
            print("NAME : {}".format(user_to_view))
            print("GENDER : {}".format(utility.READER_GENDERS[int(user_info_split[1])]))
            print("AGE RANGE : {}".format(utility.READER_AGES[int(user_info_split[2])]))
            print("FAVOURITE TYPE OF BOOK : {}".format(utility.BOOK_GENRES[int(user_info_split[3])]))

            # VIEW USER INFO IN BOOKS_READ.TXT

            print("This user has read the following book :")

            ''' Like done previously, with the does_reader_exist, we can access the line of that user in the 
                list_of_all_booksread_lines. We then split that line into a list, 
                to access the values of the line separately.'''
            user_info_split = list_of_booksread_lines[does_reader_exist].split(",")
            ''' This loop will allow us to see, for each number attributed in booksread (for the reader that we want to 
            view), which book (as a string) it correspond to. '''
            for i in range(1, len(user_info_split)):
                books_list = open("books.txt", "r", encoding="UTF-8")
                # We remove the \n in the list from the readlines() command
                list_of_books = utility.remove_gap(books_list.readlines())
                # we initialized number_assigned_to_deleted_book to create the while loop
                found_book, position_of_book = False, 0
                # The while loop stops when we found which book title is attributed to the current number that the for
                # loop is running
                while found_book == False and position_of_book < len(list_of_books):
                    if int(user_info_split[i]) == position_of_book:
                        print("- ", list_of_books[position_of_book])
                        found_book = True
                    position_of_book += 1


def edit_reader_profile():
    readers_list = open("readers.txt", "r", encoding="UTF-8")
    booksread_list = open("booksread.txt", "r", encoding="UTF-8")
    list_of_all_readers = readers_list.readlines()
    list_of_booksread_users = booksread_list.readlines()
    user_to_edit = input("Which user profile do you want to edit ?\n> ")
    does_reader_exist = Check_If_User_Exists_And_Return_Rank(user_to_edit)
    if not does_reader_exist:
        print("The member that you searched doesn't exist in our database.")
    else:
        # EDIT USER INFO IN READERS LIST
        for user_info in list_of_all_readers:
            user_info_split = user_info.split(",")
            if user_info_split[0] == user_to_edit:
                parameter_to_edit = utility.FORBIDDEN_VALUE
                while parameter_to_edit <= 0 or parameter_to_edit > 5:
                    print("""Which parameter do you want to edit in that user's profile ? 
                                        1. Pseudonym
                                        2. Gender
                                        3. Age
                                        4. Book Type
                                        5. Book Read """)
                    parameter_to_edit = int(input("Enter the corresponding number : "))
                if parameter_to_edit == 1:
                    pseudonym = utility.ask_user_pseudonym()
                    user_info_split[0] = pseudonym
                    print(user_to_edit, "'s pseudonym has been modified to : ", pseudonym)
                elif parameter_to_edit == 2:
                    reader_gender = utility.ask_user_gender()
                    reader_gender = str(reader_gender)
                    user_info_split[1] = reader_gender
                    print(user_to_edit, 's gender is now : {}'.format(utility.READER_GENDERS[int(user_info_split[1])]))
                elif parameter_to_edit == 3:
                    reader_age = utility.ask_user_age()
                    reader_age_category = utility.user_age_category_number(reader_age)
                    reader_age_category = str(reader_age_category)
                    user_info_split[2] = reader_age_category
                    print(user_to_edit,
                          'is now in the following age range : {}'.format(utility.READER_AGES[int(user_info_split[2])]))
                elif parameter_to_edit == 4:
                    reader_book_style = utility.ask_user_book_type()
                    reader_book_style = str(reader_book_style)
                    user_info_split[3] = reader_book_style
                    print(user_to_edit,
                          'now likes the following type of book: {}'.format(
                              utility.BOOK_GENRES[int(user_info_split[3])]))
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
                    booksread_list = open("booksread.txt", "w", encoding="UTF-8")
                    booksread_list.close()
                    # Adding all the rest of readers
                    booksread_list = open("booksread.txt", "a", encoding="UTF-8")
                    for user in range(len(list_of_booksread_users)):
                        booksread_list.write(list_of_booksread_users[user])
                    booksread_list.close()
