#Page where all functions related to adding a reader are

def convert_list_to_chain(list):
    new = ""
    for x in list:
        new += str(x)
    return new

# function that asks the user for its name
def ask_user_pseudonym():
    pseudonym = input('What is your pseudonym ?\n> ')
    #for line in file_readers_read
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

# function that returns a string according to the number entered by the user for his aga
def ask_user_book_read():
    display_book
    for line in
    return book_type

def add_reader_profile():
    readers_file = open("readers.txt", "r")
    readers_file_append = open("readers.txt", "a")
    reader_pseudo = ask_user_pseudonym()
    reader_gender = ask_user_gender()
    reader_age = ask_user_age()
    reader_book_style = ask_user_book_type()
    reader_age_category = user_age_category_number(reader_age)
    readers_file_append.write(str(reader_pseudo)+str(","))
    readers_file_append.write(str(reader_gender)+str(","))
    readers_file_append.write(str(reader_age_category)+str(","))
    readers_file_append.write(str(reader_book_style)+str("\n"))
    readers_file.close()
    readers_file_append.close()

