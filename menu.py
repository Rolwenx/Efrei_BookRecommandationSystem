
from books_functions import *
from readers_functions import *
from recommandation_functions import *

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

# Function that allows the user to browse the "Managing book depository" and apply its functionalities.
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
        utility.launching_menu()

def recommendation_menu():
    print("""You are currently are on the "Recommendation" page. What do you want to do ?
    1. Rate a book
    2. Recommend a book
    3. Return to the the launch menu""")
    recommendation_menu_selection = input("Enter the corresponding choice : ")
    while recommendation_menu_selection != '1' and recommendation_menu_selection != '2' and recommendation_menu_selection != '3':
        print("You selected a nonexistent choice, choose again please.")
        recommendation_menu_selection = input("Enter the corresponding choice : ")
    recommendation_menu_selection = int(recommendation_menu_selection)
    print("\n")
    if recommendation_menu_selection == 1:
        rate_a_book()
    elif recommendation_menu_selection == 2:
        recommend_book()
    else:
        utility.launching_menu()


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

launching_menu()