from readers_functions import *
from books_functions import *
from recommandation_functions import *



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

FORBIDDEN_VALUE = -1
# List of the allowed values that the user is allowed to choose when entering his books read
list_allowed_value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']


# When doing the split, there's a \n that appears. This function will delete it
def remove_jump_of_line_in_list(list):
    for i in range(len(list)):
        list[i] = list[i][:-1]
    return list


# Function that asks the user his pseudonym
def ask_user_pseudonym():
    pseudonym = input('Enter the pseudonym ?\n')
    return pseudonym


# Function that asks the user his gender
def ask_user_gender():
    gender_number = FORBIDDEN_VALUE
    while gender_number > 3 or gender_number < 1:
        print("""Enter the gender?
           1. MAN
           2. WOMAN 
           3. NO MATTER WHAT""")
        gender_number = int(input("Enter the corresponding number : "))
    return gender_number


# function that asks the user for its age
def ask_user_age():
    age_reader = int(input("Enter the age :\n> "))
    while age_reader < 0:
        age_reader = int(
            input("Enter the age : (a valid age) \n> "))
    return age_reader


# Function that returns a number according to the age entered by the user previously
def user_age_category_number(age_reader):
    if age_reader <= 18:
        return 1
    elif age_reader > 18 and age_reader <= 25:
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

def launching_menu():
    create_scoring_matrix()
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
        recommendation_menu()
    else:
        pass