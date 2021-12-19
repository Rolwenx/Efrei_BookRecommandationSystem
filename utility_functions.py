'''---- BOOK RECOMMENDATION SYSTEM
   ---- AUTHOR : Nolwen
   ---- ROLE : Stores all the dictionaries; lists, functions that are mainly used in other files
               It also stores the launching menu that allows the user to access all functionalities of the system.'''

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

''' Function that will check if the string entered by the user is in the right format in the books read function : 
number,number,number'''


def check_if_string_is_good(string, list):
    for character in string:
        if character not in list:
            return False
    return True

'''function that ask the user his gender and will return an integer between 1 and 3 that correspond to
the gender's number in the print'''


def does_string_more_than_one_char(string):
    string = list(string)
    if len(string) > 1:
        return True
    return False


# When doing the split, there's a \n that appears. This function will delete it and return the list without it.
def remove_gap(list):
    for i in range(len(list)):
        list[-i] = list[-i][:-1]
    return list

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
        readersfunctions.reader_profiles_menu()
    elif launching_menu_selection == 2:
        book_depository_menu()
    elif launching_menu_selection == 3:
        recommendation_menu()
    else:
        pass

