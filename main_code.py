'''
---- BOOK RECOMMENDATION SYSTEM
---- AUTHOR : Yoke NGASSA
---- ROLE : Runs the main menu
'''

import time
import books_functions as booksfunctions
import readers_functions as readfunctions
import recommendation_functions as recomfunctions


def reader_profiles_menu():
    '''
    The reader's profiles menu that contains all the functionalities related to the Management of the readers profiles

    RETURNS:
        Nothing : It doesn't return anything as it's just a function to browse through the program's menu
    '''

    print("""You are currently are on the "Reader Profiles" page. What do you want to do ?
    1. Display books
    2. Add a reader
    3. View a reader
    4. Edit a reader
    5. Delete a reader
    6. Return to the the launch menu""")
    menu_selection = input("Enter the corresponding choice : ")
    while menu_selection not in ('1', '2', '3', '4', '5', '6'):
        print("You selected a nonexistent choice, choose again please.")
        menu_selection = input("Enter the corresponding choice : ")

    menu_selection = int(menu_selection)
    if menu_selection == 6:
        launching_menu()
    else:
        if menu_selection == 1:
            booksfunctions.display_list_of_book()

        elif menu_selection == 2:
            readfunctions.add_reader_profile()

        elif menu_selection == 3:
            readfunctions.view_reader_profile()

        elif menu_selection == 4:
            readfunctions.edit_reader_profile()

        elif menu_selection == 5:
            readfunctions.delete_member()

        print("\n\n")
        reader_profiles_menu()


def book_depository_menu():
    '''
    The book depository menu that contains all the functionalities related to the Management of the Book depository

    RETURNS:
        Nothing : It doesn't return anything as it's just a function to browse through the program's menu
    '''

    print("""You are currently are on the "Visit the Book Depository" page. What do you want to do ?
    1. Display books
    2. Add a book
    3. Edit a book
    4. Delete a book
    5. Return to the launch menu""")
    menu_selection = input("Enter the corresponding choice : ")
    while menu_selection not in ('1', '2', '3', '4', '5'):
        print("You selected a nonexistent choice, choose again please.")
        menu_selection = input("Enter the corresponding choice : ")

    menu_selection = int(menu_selection)
    if menu_selection == 5:
        launching_menu()
    else:
        if menu_selection == 1:
            booksfunctions.display_list_of_book()

        elif menu_selection == 2:
            booksfunctions.add_book_to_depository()

        elif menu_selection == 3:
            booksfunctions.edit_book_in_depository()

        elif menu_selection == 4:
            booksfunctions.delete_book_in_depository()

        print("\n\n")
        book_depository_menu()


def recommendation_menu():
    '''
    The recommendation menu that contains all the functionalities related to the Recommendation system

    RETURNS:
        Nothing : It doesn't return anything as it's just a function to browse through the program's menu
    '''

    print("""You are currently are on the "Recommendation" page. What do you want to do ?
    1. Rate a book
    2. Recommend a book
    3. Return to the the launch menu""")
    menu_selection = input("Enter the corresponding choice : ")
    while menu_selection not in ('1', '2', '3'):
        print("You selected a nonexistent choice, choose again please.")
        menu_selection = input("Enter the corresponding choice : ")
    menu_selection = int(menu_selection)
    if menu_selection == 3:
        launching_menu()
    else:
        if menu_selection == 1:
            recomfunctions.rate_a_book()

        elif menu_selection == 2:
            recomfunctions.recommend_book()

        print("\n\n")
        recommendation_menu()


def before_launching_menu():
    '''
    First function to be launched. Allow the user to enter the password that will 
    give them access to the code.The user will only know this password if he's an admin who has access to the README file. Doesn't return anything as
it used as an introduction function that isn't supposed to be reused elsewhere.
    '''
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
    print("Opening the system....")


def launching_menu():
    '''
    The main function of the algorithm. It regroups all three main functionalities
    and allows the user to select which functionality he wants to use. It doesn't
    return anything as it's just a function executing other functions.
    '''

    before_launching_menu()
    time.sleep(2)
    recomfunctions.create_scoring_matrix()
    print("""\nWelcome to the program! Where would you like to go ?
    1. Reader Profiles
    2. Visit the book depository
    3. Recommendation
    4. Exit the program""")
    menu_selection = input("Enter the corresponding choice : ")
    while menu_selection not in ('1', '2', '3', '4'):
        print("You selected a nonexistent choice, choose again please.")
        menu_selection = input("Enter the corresponding choice : ")
    menu_selection = int(menu_selection)
    if menu_selection == 4:
        pass
    else:
        if menu_selection == 1:
            reader_profiles_menu()

        elif menu_selection == 2:
            book_depository_menu()
        elif menu_selection == 3:
            recommendation_menu()


launching_menu()
