from Books import *
from main_code import *

def convert_list_to_chain(list):
    new = ""
    for x in list:
        new += str(x)
    return new

# function that asks the user for its name
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

def ask_user_book_read_loop():
    file_books_list = open("books.txt", "r")
    file_books_read = open("booksread.txt","a")
    print("Among the following books, which ones have you read ?"+"\n")
    list_books()
    number_book_read = input("\n"+"Enter the corresponding number : ")
    while number_book_read < '1' or number_book_read > '20':
        number_book_read = input("\n"+"Enter the corresponding number : ")
    file_books_list.write(number_book_read + str(","))
    file_books_read.close()
    file_books_list.close()

def ask_user_book_read():
    file_books_list = open("books.txt", "r")
    file_books_read = open("booksread.txt","a")
    ask_user_book_read_loop()
    print("""Do you still want to add another book to your "Have read" page ? (YES OR NO)""")
    continue_to_ask_book_read = input()
    while continue_to_ask_book_read != "Yes" or continue_to_ask_book_read != "No" or continue_to_ask_book_read != "yes" or continue_to_ask_book_read != "no" :
        continue_to_ask_book_read = input("""Do you still want to add another book to your "Have read" page ? (Yes OR No)""")
    if continue_to_ask_book_read == "Yes" or continue_to_ask_book_read == "yes" :
        ask_user_book_read_loop()
    else :
        reader_profiles_menu()
    file_books_read.close()
    file_books_list.close()

def add_reader_profile():
    readers_file = open("readers.txt", "r")
    readers_file_append = open("readers.txt", "a")
    file_books_read = open("booksread.txt", "a")
    reader_pseudo = ask_user_pseudonym()
    reader_gender = ask_user_gender()
    reader_age = ask_user_age()
    reader_book_style = ask_user_book_type()
    reader_age_category = user_age_category_number(reader_age)
    file_books_read.write(str(reader_pseudo)+",")
    ask_user_book_read()
    readers_file_append.write(str(reader_pseudo)+str(","))
    readers_file_append.write(str(reader_gender)+str(","))
    readers_file_append.write(str(reader_age_category)+str(","))
    readers_file_append.write(str(reader_book_style)+str("\n"))
    readers_file.close()
    file_books_read.close()
    readers_file_append.close()

#The user must be able to view the profile of a given reader.
#Input: the files readers.txt and booksread.txt
#Output: Display of the (human-readable) information of this reader.

def search_member_display() :
    print("Which member do you want to search ?")
    member_to_search = input("Enter his pseudonym : ")
    readers_list = open("readers.txt","r")
    for line in readers_list :
        if member_to_search in readers_list :


