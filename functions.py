# --------------------------------- ADD READER FUNCTIONS -----------------------

def ask_user_pseudonym():
    pseudonym = input('What is your pseudonym ?\n> ')
    return pseudonym

# function that asks the user for its gender
def ask_user_gender():
    gender_number = -1
    while gender_number > 3 or gender_number <1:
        print("""How do you define yourself ?
           1. MAN
           2. WOMAN 
           3. NO MATTER WHAT""")
        gender_number = int(input("Enter the number corresponding to your gender : "))
    return gender_number

def user_gender_string(gender_number):
    if gender_number == 1 :
        return 'MAN'
    elif gender_number == 2 :
        return 'WOMAN'
    else :
        return 'NO MATTER WHAT'

# function that asks the user for its age
def ask_user_age():
    age_reader = int(input("What is your age ? \n> "))
    while age_reader < 0:
        age_reader = int(input("What is your age ? You can't be less than 0 years old !!\n"))
    return age_reader

# function that gives a number according to the age entered by the user
def user_age_category_number(age_reader):
    if age_reader <= 18:
        return 1
    elif age_reader > 18 and age_reader >= 25 :
        return 2
    else :
        return 3

# function that returns a string according to the number entered by the user for his aga
def user_age_category_string(age_reader):
    if age_reader <= 18:
        return 'Less than 18 years old'
    elif age_reader > 18 and age_reader >= 25 :
        return 'Between 18 and 25 years old'
    else :
        return 'More than 25 years old'

# function that ask the user his favourite book_type
def ask_user_book_type():
    book_type = -1
    while book_type <= 0 or book_type >= 8 :
        print("""What's your reading style ?
        1. sci-fi
        2. Biography
        3. Horror
        4. Romance
        5. Fable
        6. History
        7. Comedy""")
        book_type = int(input("Enter the corresponding number : "))
    return book_type

#for add book already read, must try and do that if he enters a number already, he can't enter again
def add_reader_profile():
    #readers_file = open("readers.txt", "r")
    readers_file_append = open("readers.txt", "a")
    file_books_read = open("booksread.txt", "a")
    reader_pseudo = ask_user_pseudonym()
    reader_gender = ask_user_gender()
    reader_age = ask_user_age()
    reader_age_category = user_age_category_number(reader_age)
    reader_book_style = ask_user_book_type()
    file_books_read.write(str(reader_pseudo)+",")
    print("\n"+"Among the following books, which ones have you read ?")
    list_books()
    number_book_read = input("\n" + "Enter the corresponding number : ")

    file_books_read.write(str(number_book_read) + str(","))
    print("""Do you still want to add another book to your "Have read" page ? (YES OR NO)""")
    continue_to_ask_book_read = input()
    while continue_to_ask_book_read != "Yes" and continue_to_ask_book_read != "No" and continue_to_ask_book_read != "yes" and continue_to_ask_book_read != "no":
        print("""Do you still want to add another book to your "Have read" page ? (Yes OR No)""")
        continue_to_ask_book_read = input()
    while continue_to_ask_book_read == "Yes" or continue_to_ask_book_read == "yes":
        print("\n"+"Among the following books, which ones have you read ?")
        list_books()
        number_book_read = input("\n" + "Enter the corresponding number : ")
        file_books_read.write(str(number_book_read) + str(","))
        print("""Do you still want to add another book to your "Have read" page ? (Yes OR No)""")
        continue_to_ask_book_read = input()
        while continue_to_ask_book_read != "Yes" and continue_to_ask_book_read != "No" and continue_to_ask_book_read != "yes" and continue_to_ask_book_read != "no":
            continue_to_ask_book_read = input("""Do you still want to add another book to your "Have read" page ? (Yes OR No)""")
    file_books_read.write("\n")
    readers_file_append.write(str(reader_pseudo)+str(","))
    readers_file_append.write(str(reader_gender)+str(","))
    readers_file_append.write(str(reader_age_category)+str(","))
    readers_file_append.write(str(reader_book_style)+str("\n"))
    #readers_file.close()
    file_books_read.close()
    readers_file_append.close()

def search_member_display_readers() :
    print("Which member do you want to search ?")
    member_to_search = input("Enter his pseudonym : ")
    readers_list = open("readers.txt","r")
    for line in readers_list :
        if member_to_search in readers_list :
            content_line = readers_list.readline()
                #for character in content_line :

def delete_member() :
    print("Which member do you want to delete?")
    member_to_delete = input("Enter his pseudonym : ")
    readers_list = open("readers.txt","r")
    booksread_list = open("booksread.txt","r")
    readers_lines = readers_list.readlines()
    booksread_lines = booksread_list.readlines()
    readers_list.close()
    booksread_list.close()
    new_readers_file = open("readers.txt", "w")
    booksread_file = open("booksread.txt", "w")
    for line in readers_lines:
        if member_to_delete not in line:
            new_readers_file.write(line)
    for line2 in booksread_lines:
        if member_to_delete not in line2:
            booksread_file.write(line2)
    booksread_file.close()
    readers_list.close()





#    actions = {1: lambda: (list_books(), reader_profiles_menu()), 2: lambda: (add_reader_profile(), reader_profiles_menu()), 3: reader_profiles_menu, 4: reader_profiles_menu, 5: reader_profiles_menu, 6: reader_profiles_menu}
#    if reader_profiles_menu_selection in actions:
#        actions[reader_profiles_menu_selection]()





# --------------------------------- LAUNCHING MENU FUNCTIONS -----------------------
def launching_menu():
    print("""Welcome to our program! Where would you like to go ?
    1. Reader Profiles
    2. Visit the book depository
    3. Recommendation
    4. About the Creators""")
    launching_menu_selection = input("Enter the corresponding choice : ")
    while launching_menu_selection!= '1' and launching_menu_selection!= '2' and launching_menu_selection!= '3' and launching_menu_selection!= '4' :
        print("You selected a nonexistent choice, choose again please.")
        launching_menu_selection = input("Enter the corresponding choice : ")
    launching_menu_selection = int(launching_menu_selection)
    print("\n")
    if launching_menu_selection == 1 :
        reader_profiles_menu()
    elif launching_menu_selection == 2 :
        pass
    elif launching_menu_selection == 3 :
        pass
    else :
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
    while reader_profiles_menu_selection != '1' and reader_profiles_menu_selection != '2' and reader_profiles_menu_selection != '3' and reader_profiles_menu_selection != '4' and reader_profiles_menu_selection != '5' and reader_profiles_menu_selection != '6'  :
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
        print("\n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 3:
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 4 :
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 5 :
        delete_member()
        reader_profiles_menu()
    else :
        launching_menu()

# -------------------------------- BOOK FUNCTIONS -----------------------

def list_books():
    """Prints the list of the books preceded by the sequential number"""
    file_books_list = open("books.txt", "r")
    a = 1
    for line in file_books_list:
        print(a,') ',line,end='')
        a+=1
    file_books_list.close()
