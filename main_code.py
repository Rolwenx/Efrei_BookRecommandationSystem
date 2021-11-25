from add_reader import *
from Books import *

def launching_menu() :
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
        print("\n \n")
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 3:
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 4 :
        reader_profiles_menu()
    elif reader_profiles_menu_selection == 5 :
        reader_profiles_menu()
    else :
        launching_menu()

launching_menu()

