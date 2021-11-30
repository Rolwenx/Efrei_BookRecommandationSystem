# DICTIONARIES CREATED
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

BOOK_DEPOSITORY = {
    1: 'Débuter la programmation Java',
    2: 'Apprendre Python',
    3: 'Les Citations du Président Mao Tse-Toung',
    4: 'Don Quichotte de la Manche',
    5: 'Un conte de deux villes',
    6: 'Le Seigneur des Anneaux',
    7: 'Le Petit Prince',
    8: 'Harry Potter à l’école des sorciers',
    9: 'Le Seigneur des Anneaux'
}

DELIMITER = ','
LINE_BREAK = '\n\t'
FORBIDDEN_VALUE = -1

# --------------------------------- ADD READER FUNCTIONS -----------------------


def ask_user_pseudonym():
    pseudonym = input('What is your pseudonym ?\n')
    return pseudonym



# function that asks the user for its gender
def ask_user_gender():
    gender_number = -1
    while gender_number > 3 or gender_number < 1:
        print("""How do you define yourself ?
           1. MAN
           2. WOMAN 
           3. NO MATTER WHAT""")
        gender_number = int(
            input("Enter the number corresponding to your gender : "))
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
    age_reader = int(input("What is your age ? \n> "))
    while age_reader < 0:
        age_reader = int(
            input("What is your age ? You can't be less than 0 years old !!\n"))
    return age_reader


# function that gives a number according to the age entered by the user
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
        print("""What's your reading style ?
        1. Sci-fi
        2. Biography
        3. Horror
        4. Romance
        5. Fable
        6. History
        7. Comedy""")
        book_type = int(input("Enter the corresponding number : "))
    return book_type


def bookread_reader_profile():
    file_books_read = open("booksread.txt", "a")
    list_of_booksread = []
    print("\n" + "Among the following books, which ones have you read ?")
    list_books()
    number_book_read = input("\n" + "Enter the corresponding number : ")
    list_of_booksread.append(number_book_read)
    file_books_read.write(str(number_book_read) + str(","))
    print("""Do you still want to add another book to your "Have read" page ? (YES OR NO)\n> """)
    continue_to_ask_book_read = input()
    while continue_to_ask_book_read != "Yes" and continue_to_ask_book_read != "No" and continue_to_ask_book_read != "yes" and continue_to_ask_book_read != "no":
        print("""Do you still want to add another book to your "Have read" page ? (Yes OR No)""")
        continue_to_ask_book_read = input()
    while continue_to_ask_book_read == "Yes" or continue_to_ask_book_read == "yes":
        print("\n" + "Among the following books, which ones have you read ?")
        list_books()
        number_book_read = input("\n" + "Enter the corresponding number : ")
        while number_book_read in list_of_booksread:
            print("You already selected this book. Choose again")
            number_book_read = input("\n" + "Enter the corresponding number : ")
        list_of_booksread.append(number_book_read)
        file_books_read.write(str(number_book_read) + str(","))
        print("""Do you still want to add another book to your "Have read" page ? (Yes OR No)""")
        continue_to_ask_book_read = input()
        while continue_to_ask_book_read != "Yes" and continue_to_ask_book_read != "No" and continue_to_ask_book_read != "yes" and continue_to_ask_book_read != "no":
            continue_to_ask_book_read = input("""Do you still want to add another book to your "Have read" page ? (Yes OR No)""")
    del list_of_booksread[:]


# for add book already read, must try and do that if he enters a number already, he can't enter again
def add_reader_profile():
    # readers_file = open("readers.txt", "r")
    readers_file_append = open("readers.txt", "a")
    file_books_read = open("booksread.txt", "a")
    reader_pseudo = ask_user_pseudonym()
    reader_gender = ask_user_gender()
    reader_age = ask_user_age()
    reader_age_category = user_age_category_number(reader_age)
    reader_book_style = ask_user_book_type()
    file_books_read.write(str(reader_pseudo) + ",")
    file_books_read.write(str("\n"))
    bookread_reader_profile()
    readers_file_append.write(str(reader_pseudo) + str(",")+str(reader_gender) + str(","))
    readers_file_append.write(str(reader_age_category) + str(","))
    readers_file_append.write(str(reader_book_style) + str("\n"))
    # readers_file.close()
    file_books_read.close()
    readers_file_append.close()

def delete_member():
    print("Which member do you want to delete?")
    member_to_delete = input("Enter their pseudonym : ")
    readers_list = open("readers.txt", "r")
    booksread_list = open("booksread.txt", "r")
    readers_lines = readers_list.readlines()
    booksread_lines = booksread_list.readlines()
    found = False
    for i in readers_lines :
        readers_line = i.split(",")
        if member_to_delete in readers_line :
            found = True
            readers_list = open("readers.txt","w")
            booksread_list = open("booksread.txt","w")
            for line in readers_lines :
                if member_to_delete not in  line :
                    readers_list.write(line)
            for line2 in booksread_lines:
                if member_to_delete not in line2:
                    booksread_list.write(line2)
            print("Member successfully deleted.")
    if found == False :
            print("Member not found in our database.")
    readers_list.close()
    booksread_list.close()


def parse_user_info(txt_line):
    infos = txt_line.split(DELIMITER)
    for i in range(len(infos)):
        if i != 0:
            infos[i] = int(infos[i])

    return infos


def view_reader_profile():
    with open("readers.txt", "r") as readers_list, open("booksread.txt","r") as booksread_list :
        list_of_all_readers = tuple(map(parse_user_info, readers_list.readlines()))
        list_of_all_booksreads_by_readers = tuple(map(parse_user_info, readers_list.readlines()))
    found = False
    user_query = str(input("Which member do you want to search for? Enter the pseudonym: "))
    for user_info in list_of_all_readers:
        if user_info[0] == user_query:
            print(f"""\n{user_info[0]} has for gender: {READER_GENDERS[user_info[1]]}
{user_info[0]} is in the following age range: {READER_AGES[user_info[2]]}
{user_info[0]} likes the following type of book: {BOOK_GENRES[user_info[3]]}\n""")
            #for i in
            found = True
            # break
    if not found:
        print("The member that you searched doesn't exist in our database.\n")


def edit_reader_profile():
    print("Which profile do you want to edit ?")
    reader_to_search = input("Enter the pseudonym : ")
    readers_list = open("readers.txt", "r")
    #booksread_list = open("booksread.txt", "r")
    found = False
    list_of_all_readers = readers_list.readlines()
    for i in list_of_all_readers:
        reader_to_view = i.split(",")
        if reader_to_search in reader_to_view:
            PARAMETER_TO_EDIT = FORBIDDEN_VALUE
            while PARAMETER_TO_EDIT <= 0 or PARAMETER_TO_EDIT >= 8:
                print("""Which parameter do you want to edit in that user's profile ? 
                1. Pseudonym
                2. Gender
                3. Age
                4. Book Type
                5. Book Read """)
                PARAMETER_TO_EDIT = int(input("Enter the corresponding number : "))
                if PARAMETER_TO_EDIT == 1:
                    pseudonym = ask_user_pseudonym()
                    reader_to_view[0] = pseudonym
                elif PARAMETER_TO_EDIT == 2:
                    reader_gender = ask_user_gender()
                    reader_to_view[1] = reader_gender
                elif PARAMETER_TO_EDIT == 3:
                    reader_age = ask_user_age()
                    reader_age_category = user_age_category_number(reader_age)
                    reader_to_view[2] = reader_age_category
                elif PARAMETER_TO_EDIT == 4:
                    reader_book_style = ask_user_book_type()
                    reader_to_view[3] = reader_book_style
                else:
                    pass
            print(f"""{reader_to_view[0]} has for gender: {READER_GENDERS[reader_to_view[1]]}
                {reader_to_view[0]} is in the following age range: {READER_AGES[reader_to_view[2]]}
                {reader_to_view[0]} likes the following type of book: {BOOK_GENRES[reader_to_view[3]]}"""
                  )
            found = True
    if not found:
        print("The member that you searched doesn't exist in our database. \n")
    readers_list.close()


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
        pass
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
        reader_profiles_menu_selection = input( "Enter the corresponding choice : ")
    reader_profiles_menu_selection = int(reader_profiles_menu_selection)
    print("\n")

    if reader_profiles_menu_selection == 1:
        list_books()
        print("\n \n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 2:
        add_reader_profile()
        print("\n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 3:
        view_reader_profile()
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 4:
        edit_reader_profile()
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 5:
        delete_member()
        reader_profiles_menu()
    else:
        launching_menu()


# -------------------------------- BOOK FUNCTIONS -----------------------

def list_books():
    """Prints the list of the books preceded by the sequential number"""
    file_books_list = open("books.txt", "r")
    a = 1
    for line in file_books_list:
        print(a, ') ', line, end='')
        a += 1
    file_books_list.close()
