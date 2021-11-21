#Readers
#Projet Python Yoke Joseph BOOKS
file_readers_append = file_books = open("readers.txt", "a")
file_readers_read = file_books = open("readers.txt", "r")

def convert_list_to_chain(list):
    new = ""
    for x in list:
        new += str(x)
    return new

# function that asks the user for its name
def name_reader_function():
    pseudonym = input('What is your pseudonym ?\n> ')
    #for line in file_readers_read
    return pseudonym

# function that asks the user for its gender
def gender_reader_function():
    gender_number = -1
    while gender_number > 3 or gender_number <1:
        print("""How do you define yourself ?
           1) MAN
           2) WOMAN 
           3) NO MATTER WHAT""")
        gender_number = int(input("Enter the number corresponding to your gender : "))
    return gender_number

# function that returns a string according to the number entered by the user for his gender
#def gender_reader_inverse_function(a):
#    if a == 1:
#        return 'MAN'
#    elif a == 2:
#        return 'WOMAN'
#   else:
#        return 'Undefined gender'

# function that asks the user for its age
def age_reader_function():
    age_reader = int(input("What is your age ? \n> "))
    while age_reader < 0:
        age_reader = int(input("What is your age ? You can't be less than 0 years old !!\n"))
    return age_reader

# function that gives a number according to the age entered by the user
def age_reader_category_function(age_reader):
    if age_reader <= 18:
        return 1
    elif age_reader > 18 and age_reader >= 25 :
        return 2
    else :
        return 3

# function that returns a string according to the number entered by the user for his aga
def age_reader_category_inverse_function(age_reader):
    if age_reader <= 18:
        return 'Less than 18 years old'
    elif age_reader > 18 and age_reader >= 25 :
        return 'Between 18 and 25 years old'
    else :
        return 'More than 25 years old'



reader_pseudo = name_reader_function()
reader_gender = gender_reader_function()
reader_age = age_reader_function()
reader_age_category = age_reader_category_function(reader_age)
file_readers_append.write(str(reader_pseudo)+str(","))
file_readers_append.write(str(reader_gender)+str(","))
file_readers_append.write(str(reader_age_category)+str(",")+str("\n"))
file_readers_append.close()
file_readers_read.close()