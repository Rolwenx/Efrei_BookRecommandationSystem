'''---- BOOK RECOMMENDATION SYSTEM
   ---- AUTHOR : Nolwen
   ---- ROLE : Stores all the dictionaries; lists, functions that are mainly used in other files
               It also stores the launching menu that allows the user to access all functionalities of the system.'''

from readers_functions import *
from recommandation_functions import *


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
