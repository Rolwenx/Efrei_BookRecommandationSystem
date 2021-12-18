from readers_functions import *
from recommandation_functions import *
import time

FORBIDDEN_VALUE = -1

# Another list of allowed values but this times without the ',' for the add_reader_function where we only need number
list_allowed_value2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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


# Function that asks the user his pseudonym and return it as a string
def ask_user_pseudonym():
    list_forbidden_value = [' ']
    pseudonym = input('Enter the pseudonym ?\n')
    while  len(pseudonym) == 0 or check_if_string_is_good(pseudonym, list_forbidden_value) == True:
        print("You didn't enter anything. Please enter something.")
        pseudonym = input('Enter the pseudonym ?\n')
    return pseudonym


'''function that ask the user his gender and will return an integer between 1 and 3 that correspond to
the gender's number in the print'''


def does_string_more_than_one_char(string):
    string = list(string)
    if len(string) > 1:
        return True
    return False

def remove_gap(list):
    for i in range(len(list)):
        list[-i] = list[-i][:-1]
    return list

def ask_user_gender():
    list_allowed_value = ['1', '2', '3']
    print("""Enter the gender?
               1. MAN
               2. WOMAN 
               3. NO MATTER WHAT""")
    gender_number = input("Enter the corresponding number : ")
    while check_if_string_is_good(gender_number, list_allowed_value) == False or does_string_more_than_one_char(
            gender_number) == True:
        print("You didn't respect the wanted format of answer or entered a letter.")
        gender_number = input("Enter the correct corresponding number : ")
    while  len(gender_number) == 0 :
        print("You didn't enter anything. Please enter something.")
        gender_number = input("Enter the correct corresponding number: ")
    gender_number = int(gender_number)
    return gender_number


# function that asks the user for its age and returns that number as an integer
def ask_user_age():
    list_allowed_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    age_reader = input("Enter the age :\n> ")
    while not check_if_string_is_good(age_reader, list_allowed_value):
        print("You didn't respect the wanted format of answer or entered a letter.")
        age_reader = input("Enter a number and not a letter : ")
        check_if_string_is_good(age_reader)
    while  len(age_reader) == 0 :
        print("You didn't enter anything. Please enter something.")
        age_reader = input("Enter a number and not a letter : ")
    age_reader = int(age_reader)
    return age_reader


# Function that returns a number according to the age entered by the user in the previous function
def user_age_category_number(age_reader):
    if age_reader <= 18:
        return 1
    elif 18 < age_reader <= 25:
        return 2
    else:
        return 3


'''function that ask the user his favourite book_type and will return an integer between 0 and 8 that correspond to
the book style's number in the print'''


def ask_user_book_type():
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
    while check_if_string_is_good(book_type, list_allowed_value) == False or does_string_more_than_one_char(
            book_type) == True :
        print("You didn't respect the wanted format of answer or entered a letter.")
        book_type = input("Enter the correct corresponding number: ")
    while  len(book_type) == 0 :
        print("You didn't enter anything. Please enter something.")
        book_type = input("Enter the correct corresponding number: ")
    book_type = int(book_type)
    return book_type


'''First function to be launched. Allow the user to enter the password that will give him access to the code. 
The user will only know this password if he's an admin who has access to the README file. Doesn't return anything as
it used as an introduction function that isn't supposed to be reused elsewhere.'''

'''def before_launching_menu():
    print("Welcome.")
    time.sleep(1.5)
    password = input("Enter the password to access the system :\n> ")
    while password != "iamthebesteacherintheworld":
        print("Wrong password. Perhaps, read the README.txt file.")
        password = input("Enter the password to access the system :\n> ")
    print("Permission given.")
    time.sleep(1)
    print("You can now access the system.")
    time.sleep(0.5)
    print("Opening the system....")'''

'''The main function of the algorithm. It regroups all three main functionalities and allows the user to select which
 functionality he wants to use. It doesn't return anything as it's just a function executing other functions.'''


def launching_menu():
    # before_launching_menu()
    # time.sleep(2)
    create_scoring_matrix()
    print("""\nWelcome to the program! Where would you like to go ?
    1. Reader Profiles
    2. Visit the book depository
    3. Recommendation
    4. Exit the program""")
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
        recommendation_menu()
    else:
        pass
