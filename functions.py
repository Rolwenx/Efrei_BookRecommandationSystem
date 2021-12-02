# DICTIONARIES CREATED
from curses.ascii import isdigit

READER_GENDERS = {
    1: "MAN",
    2: "WOMAN",
    3: "NO MATTER WHAT"
}

READER_AGES = {
    1: "Less than 18 years old",
    2: "Between 18 and 25 years old",
    3: "More than 25 years old"
}

BOOK_GENRES = {
    1: 'Sci-fi',
    2: 'Biography',
    3: 'Horror',
    4: 'Romance',
    5: 'Fable',
    6: 'History',
    7: 'Comedy'
}

DELIMITER = ','
LINE_BREAK = '\n\t'
FORBIDDEN_VALUE = -1


def remove_jump_of_line_in_list(list):
    for i in range(len(list)):
        list[i] = list[i][:-1]
    return list


# --------------------------------- ADD READER FUNCTIONS -----------------------


def ask_user_pseudonym():
    pseudonym = input('Enter the pseudonym ?\n')
    return pseudonym


def ask_user_gender():
    gender_number = FORBIDDEN_VALUE
    while gender_number > 3 or gender_number < 1:
        print("""Enter the gender?
           1. MAN
           2. WOMAN 
           3. NO MATTER WHAT""")
        gender_number = int(input("Enter the corresponding number : "))
    return gender_number


def user_gender_string(gender_number):
    if gender_number == 1:
        return 'MAN'
    elif gender_number == 2:
        return 'WOMAN'
    else:
        return 'NO MATTER WHAT'


# function that asks the user for its age
def ask_user_age():
    age_reader = int(input("Enter the age :\n> "))
    while age_reader < 0:
        age_reader = int(
            input("Enter the age : (a valid age) \n> "))
    return age_reader


def user_age_category_number(age_reader):
    if age_reader <= 18:
        return 1
    elif age_reader > 18 and age_reader >= 25:
        return 2
    else:
        return 3


# function that ask the user his favourite book_type
def ask_user_book_type():
    book_type = FORBIDDEN_VALUE
    while book_type <= 0 or book_type >= 8:
        print("""What is the reading style among those ? :
        1. Sci-fi
        2. Biography
        3. Horror
        4. Romance
        5. Fable
        6. History
        7. Comedy""")
        book_type = int(input("Enter the corresponding number: "))
    return book_type


def check_if_string_is_digit(string):
    is_it_digit = string.isdigit()
    if is_it_digit:
        return True
    else:
        return False


def enter_number_in_books_read():
    list_books()
    number_of_the_book_read = 'Forbidden'
    is_it_a_number = check_if_string_is_digit(number_of_the_book_read)
    while not is_it_a_number:
        number_of_the_book_read = input("\n" + "Enter the corresponding number : ")
        is_it_a_number = check_if_string_is_digit(number_of_the_book_read)
    return number_of_the_book_read


#################################################
def book_read_reader_profile():
    file_books_read = open("booksread.txt", "a")
    list_of_booksread = []
    print("\n" + "Among the following books, which ones have you read ?")
    number_of_the_book_read = enter_number_in_books_read()
    list_of_booksread.append(number_of_the_book_read)
    file_books_read.write(str(number_of_the_book_read) + str(","))
    print("""Do you still want to add another book to your "Have read" page ? (YES OR NO""")
    continue_to_ask_book_read = input("> ")
    while continue_to_ask_book_read != "Yes" and continue_to_ask_book_read != "No" and continue_to_ask_book_read != "yes" and continue_to_ask_book_read != "no":
        print("""Do you still want to add another book that you've read ? (Yes OR No)""")
        continue_to_ask_book_read = input("> ")
    while continue_to_ask_book_read == "Yes" or continue_to_ask_book_read == "yes":
        print("\n" + "Among the following books, which ones have you read ?")
        number_of_the_book_read = enter_number_in_books_read()
        while number_of_the_book_read in list_of_booksread:
            print("You already selected this book. Choose again")
            number_book_read = input("\n" + "Enter the corresponding number : ")
        list_of_booksread.append(number_book_read)
        file_books_read.write(str(number_book_read) + str(","))
        print("""Do you still want to add another book that you've read ? (Yes OR No)""")
        continue_to_ask_book_read = input("> ")
        while continue_to_ask_book_read != "Yes" and continue_to_ask_book_read != "No" and continue_to_ask_book_read != "yes" and continue_to_ask_book_read != "no":
            continue_to_ask_book_read = input(
                """Do you still want to add another book that you've read ? (Yes OR No)\n> """)
    del list_of_booksread[:]


def add_reader_profile():
    readers_file_append = open("readers.txt", "a")
    file_books_read = open("booksread.txt", "a")
    condition_of_existence = check_if_user_already_exist()
    if not condition_of_existence:
        reader_gender = ask_user_gender()
        reader_age = ask_user_age()
        reader_age_category = user_age_category_number(reader_age)
        reader_book_style = ask_user_book_type()
        book_read_reader_profile()
        readers_file_append.write(str(reader_gender) + str(",") + str(reader_age_category) + str(","))
        readers_file_append.write(str(reader_book_style) + str("\n"))
    else:
        print("This user already exist.")
    file_books_read.close()
    readers_file_append.close()


def check_if_user_already_exist():
    reader_pseudo = ask_user_pseudonym()
    with open("readers.txt", "r") as readers_list_checkers:
        readers_in_list = readers_list_checkers.readlines()
    with open("readers.txt", "a") as readers_file_append, open("booksread.txt", "a") as file_books_read:
        readers_file_append.write(str(reader_pseudo) + str(","))
        file_books_read.write(str(reader_pseudo) + str(","))
        for user in readers_in_list:
            user_split = user.replace(',', " ").split()
            if user_split == reader_pseudo:
                return True
    return False


def delete_member():
    print("Which member do you want to delete?")
    member_to_delete = input("Enter their pseudonym : ")
    readers_list = open("readers.txt", "r")
    books_read_list = open("booksread.txt", "r")
    readers_lines = readers_list.readlines()
    books_read_lines = books_read_list.readlines()
    found = False
    for i in readers_lines:
        readers_line = i.split(",")
        if member_to_delete in readers_line:
            found = True
            readers_list = open("readers.txt", "w")
            books_read_list = open("booksread.txt", "w")
            for line in readers_lines:
                if member_to_delete not in line:
                    readers_list.write(line)
            for line2 in books_read_lines:
                if member_to_delete not in line2:
                    books_read_list.write(line2)
            print("Member successfully deleted.")
    if not found:
        print("Member not found in our database.")
    readers_list.close()
    books_read_list.close()


def parse_user_info(txt_line):
    infos = txt_line.split(DELIMITER)
    for i in range(len(infos)):
        if i != 0:
            infos[i] = int(infos[i])
    return infos


#################################################
def view_reader_profile():
    with open("readers.txt", "r") as readers_list:
        list_of_all_readers = tuple(map(parse_user_info, readers_list.readlines()))
        found = False
    user_query = str(input("Which member do you want to search for? Enter the pseudonym: "))
    for user_info in list_of_all_readers:
        if user_info[0] == user_query:
            print(f"""\n{user_info[0]} has for gender: {READER_GENDERS[user_info[1]]}
{user_info[0]} is in the following age range: {READER_AGES[user_info[2]]}
{user_info[0]} likes the following type of book: {BOOK_GENRES[user_info[3]]}\n""")
            found = True
    if not found:
        print("The member that you searched doesn't exist in our database.\n")


def edit_reader_profile():
    with open("readers.txt", "r") as readers_list, open("booksread.txt", "r") as booksread_list:
        list_of_all_readers = tuple(map(parse_user_info, readers_list.readlines()))
        # list_of_all_booksreads_by_readers = tuple(map(parse_user_info, booksread_list.readlines()))
        print(list_of_all_readers)
    found = False
    user_to_edit = str(input("Which profile do you want to edit ? Enter the pseudonym: "))
    for user_info in list_of_all_readers:
        if user_info[0] == user_to_edit:
            PARAMETER_TO_EDIT = FORBIDDEN_VALUE
            while PARAMETER_TO_EDIT <= 0 or PARAMETER_TO_EDIT > 5:
                print("""Which parameter do you want to edit in that user's profile ? 
                            1. Pseudonym
                            2. Gender
                            3. Age
                            4. Book Type
                            5. Book Read """)
                PARAMETER_TO_EDIT = int(input("Enter the corresponding number : "))
            if PARAMETER_TO_EDIT == 1:
                pseudonym = ask_user_pseudonym()
                user_info[0] = pseudonym
                print(user_to_edit, "'s pseudonym has been modified to : ", pseudonym)
            elif PARAMETER_TO_EDIT == 2:
                reader_gender = ask_user_gender()
                user_info[1] = reader_gender
                print(f"""\n{user_info[0]} has for gender: {READER_GENDERS[user_info[1]]}""")
            elif PARAMETER_TO_EDIT == 3:
                reader_age = ask_user_age()
                reader_age_category = user_age_category_number(reader_age)
                user_info[2] = reader_age_category
                print(f"""{user_info[0]} is in the following age range: {READER_AGES[user_info[2]]}""")
            elif PARAMETER_TO_EDIT == 4:
                reader_book_style = ask_user_book_type()
                user_info[3] = reader_book_style
                print(f"""{user_info[0]} likes the following type of book: {BOOK_GENRES[user_info[3]]}\n""")
            else:
                pass
            found = True
        readers_list = open("readers.txt", "w")
        for list in list_of_all_readers:
            for element in list:
                readers_list.write(str(element) + str(","))
        readers_list.close()

    if not found:
        print("The member that you searched doesn't exist in our database. \n")


# -------------------------------- BOOK FUNCTIONS -----------------------

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
        list_of_books = remove_jump_of_line_in_list(books_list.readlines())
        found_book_to_delete, number_assigned_to_deleted_book = False, 0
        while found_book_to_delete == False and number_assigned_to_deleted_book < len(list_of_books):
            if book_title_to_delete == list_of_books[number_assigned_to_deleted_book]:
                del list_of_books[number_assigned_to_deleted_book]
                temp_number = number_assigned_to_deleted_book + 1
            number_assigned_to_deleted_book += 1
        with open("books.txt", "w") as books_list:
            for books in list_of_books:
                books_list.write(str(books) + str("\n"))
            print("The selected book has been deleted.")
        # DELETE THE BOOK NUMBER FOR THE USER WHO READ THE DELETED BOOK
        with open("booksread.txt", "r") as books_read:
            booksread_users = remove_jump_of_line_in_list(books_read.readlines())
            for i in range(len(booksread_users)):
                user = booksread_users[i].split(',')
                for j in range(len(user)):
                    temp_number = str(temp_number)
                    if user[j] == temp_number:
                        del user[j]
                booksread_users[i] = ",".join(user)
        with open("booksread.txt", "w") as books_read:
            for user in booksread_users:
                print(user)
                # books_read.write(str(user) + str("\n"))
    else:
        print("This book is not in the depository. Can't delete a non-existent book.")


# --------------------------------- LAUNCHING MENU FUNCTIONS -----------------------

def launching_menu():
    print("""Welcome to our program! Where would you like to go ?
    1. Reader Profiles
    2. Visit the book depository
    3. Recommendation
    4. About the Creators""")
    launching_menu_selection = input("Enter the corresponding choice : ")
    while launching_menu_selection != '1' and launching_menu_selection != '2' and launching_menu_selection != '3' and launching_menu_selection != '4':
        print("You selected a nonexistent choice, choose again please.")
        launching_menu_selection = input("Enter the corresponding choice : ")
    launching_menu_selection = int(launching_menu_selection)
    print("\n")
    if launching_menu_selection == 1:
        reader_profiles_menu()
    elif launching_menu_selection == 2:
        book_depository_menu()
    elif launching_menu_selection == 3:
        pass
    else:
        pass


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
