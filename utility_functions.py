'''
---- BOOK RECOMMENDATION SYSTEM
---- AUTHOR : Yoke NGASSA
---- ROLE : Stores all the functions that are mainly used in other files
            Also stores the launching menu that allows the user to access
            all functionalities of the system.
'''


def is_string_correct_format(string, list):
    '''
    Function that will check if the string entered by the user is in the right format
    (with values included in the list).

    PARAMETERS:
        < string > (string): The string which Input should be in the good format.

    RETURNS:
        < condition > (boolean) : Returns True if the string is in the correct format.
        Else false.
    '''
    for character in string:
        if character not in list:
            return False

    return True


def more_than_1_char(string):
    '''
    Function used for 1 character Inputs. It checks if the Input only has one character

    PARAMETERS:
        < string > (string): The string which Input should only be one character

    RETURNS:
        < condition > (boolean) : Return True if string has more than one character.
        Else return False
    '''
    string = list(string)
    if len(string) > 1:
        return True
    return False


def remove_gap(list_of_strings):
    '''
    When creating a list, sometimes a \n appears if the string converted into
    a list had a jump of line. This function removes it.

    PARAMETERS:
        < list_of_strings > (list): The list with the \n at the end of some items

    RETURNS:
        < list_of_strings > (list): The list without the \n at the end of some items
    '''

    for i, string in enumerate(list_of_strings):
        if string[-1] == "\n":
            list_of_strings[i] = string[:-1]

    return list_of_strings
