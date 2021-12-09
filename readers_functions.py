from utilitary_functions import *

# Function that will check if the string entered by the user is in the right format in the books read function
def check_if_string_is_good(string):
    for character in string:
        if character not in list_allowed_value:
            return False
    return True


# Function that will ask the user to enter the books that he has read
def book_read_reader_profile():
    print("\n" + "Among the following books, which ones have you read ?")
    list_books()
    books_read_list = input("Enter the numbers corresponding to the books (separated by commas. Ex : 1,2,4)\n> ")
    while not check_if_string_is_good(books_read_list):
        print("You didn't respect the wanted format of answer or entered a letter.")
        books_read_list = input("Enter the numbers in the correct format (separated by commas. Ex : 1,2,4)\n> ")
        check_if_string_is_good(books_read_list)
    return books_read_list

# Global function that will check if a user exists in the readers.txt file
def check_if_user_already_exist(pseudo):
    with open("readers.txt", "r") as readers_list_checkers:
        readers_in_list = readers_list_checkers.readlines()
        for user in readers_in_list:
            user_split = user.split(",")
            if user_split[0] == pseudo:
                return True
    return False

# Function that will add a reader
def add_reader_profile():
    readers_file_append = open("readers.txt", "a")
    file_books_read = open("booksread.txt", "a")
    reader_pseudo = ask_user_pseudonym()
    if not check_if_user_already_exist(reader_pseudo):
        reader_gender = ask_user_gender()
        reader_age = ask_user_age()
        reader_age_category = user_age_category_number(reader_age)
        reader_book_style = ask_user_book_type()
        enter_books_read = book_read_reader_profile()
        readers_file_append.write(str(reader_pseudo) + str(","))
        file_books_read.write(str(reader_pseudo) + str(",") + str(enter_books_read) + str("\n"))
        readers_file_append.write(str(reader_gender) + str(",") + str(reader_age_category) + str(","))
        readers_file_append.write(str(reader_book_style) + str("\n"))
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
    if check_if_user_already_exist(member_to_delete):
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
    else:
        print("Member not found in our database.")
    readers_list.close()
    books_read_list.close()


def view_reader_profile():
    with open("readers.txt", "r") as readers_list, open("booksread.txt","r") as booksread_list:
        list_of_all_readers = readers_list.readlines()
        list_of_booksread_lines = booksread_list.readlines()
        user_to_view = input("Which user do you want to view ?\n> ")
        if check_if_user_already_exist(user_to_view):
            # VIEW USER INFO IN READERS.TXT
            for user_info in list_of_all_readers:
                user_info_split = user_info.split(",")
                if user_info_split[0] == user_to_view:
                    print("NAME : {}".format(user_to_view))
                    print("GENDER : {}".format(READER_GENDERS[int(user_info_split[1])]))
                    print("AGE RANGE : {}".format(READER_AGES[int(user_info_split[2])]))
                    print("FAVOURITE TYPE OF BOOK : {}".format(BOOK_GENRES[int(user_info_split[3])]))
            # VIEW USER INFO IN BOOKS_READ.TXT
            # for user_info_in_booksread in list_of_booksread_lines:
            #  user_info_split = user_info_in_booksread.split(",")
            #  if user_info_split[0] == user_to_view:
        else:
            print("The member that you searched doesn't exist in our database.")


def edit_reader_profile():
    readers_list = open("readers.txt", "r")
    list_of_all_readers = readers_list.readlines()
    user_to_edit = input("Which user profile do you want to edit ?\n> ")
    if check_if_user_already_exist(user_to_edit):
        # EDIT USER INFO IN READERS LIST
        for user_info in list_of_all_readers:
            user_info_split = user_info.split(",")
            if user_info_split[0] == user_to_edit:
                parameter_to_edit = FORBIDDEN_VALUE
                while parameter_to_edit <= 0 or parameter_to_edit > 5:
                    print("""Which parameter do you want to edit in that user's profile ? 
                                1. Pseudonym
                                2. Gender
                                3. Age
                                4. Book Type
                                5. Book Read """)
                    parameter_to_edit = int(input("Enter the corresponding number : "))
                if parameter_to_edit == 1:
                    pseudonym = ask_user_pseudonym()
                    user_info_split[0] = pseudonym
                    print(user_to_edit, "'s pseudonym has been modified to : ", pseudonym)
                elif parameter_to_edit == 2:
                    reader_gender = ask_user_gender()
                    reader_gender = str(reader_gender)
                    user_info_split[1] = reader_gender
                    print(user_to_edit, 's gender is now : {}'.format(READER_GENDERS[int(user_info_split[1])]))
                elif parameter_to_edit == 3:
                    reader_age = ask_user_age()
                    reader_age_category = user_age_category_number(reader_age)
                    reader_age_category = str(reader_age_category)
                    user_info_split[2] = reader_age_category
                    print(user_to_edit,
                          'is now in the following age range : {}'.format(READER_AGES[int(user_info_split[2])]))
                elif parameter_to_edit == 4:
                    reader_book_style = ask_user_book_type()
                    reader_book_style = str(reader_book_style)
                    user_info_split[3] = reader_book_style
                    print(user_to_edit,
                          'now likes the following type of book: {}'.format(BOOK_GENRES[int(user_info_split[3])]))
                else:
                    pass
                readers_list.close()
                # Adding the new info about the user that we wanted to edit in booksread.txt and readers.txt
                readers_list = open("readers.txt", "w")
                readers_list.close()
            # Adding all the rest of readers
            readers_list = open("readers.txt", "a")
            joining_user = ",".join(user_info_split)
            readers_list.write(joining_user)
            readers_list.close()
    else:
        print("The member that you searched doesn't exist in our database.")


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
        launching_menu()
