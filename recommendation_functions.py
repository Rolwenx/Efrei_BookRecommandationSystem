'''------------------ RECOMMENDATION BOOK FUNCTIONS ---------------
---- BOOK RECOMMENDATION SYSTEM
---- AUTHOR: Yoke NGASSA & Joseph Bénard
---- ROLE: Stores all the functionalities related to the Recommendation Sytem
        such as:
        - Rate a book
        - Recommend a book
        - Create a scoring matrix
    + the functions related to those functionalities
'''
# from books_functions import *
import math

import readers_functions
import utility_functions as utility
from readers_functions import get_user_index
import books_functions as booksfunctions


def create_scoring_matrix():
    '''
    Function to create the scoring matrix that will be initialized the first time
    that the program will be launched. It will write/create a scoring matrix file
    whenever it doesn't exists to conserve the data.

    PARAMETERS:
        < Nothing >: The function doesn't need parameters for creating a scoring matrix
        since it opens book and reader files and use it for creating the matrix

    RETURNS:
        < Nothing >: The function instead creates a matrix in a file but returns nothing .
    '''

    with open("books.txt", "r") as books_file, open("readers.txt", 'r') as readers_file:
        nbRow = len(readers_file.readlines())
        nbCol = len(books_file.readlines())
        matrix = [['0'] * nbCol] * nbRow
    try:
        scoring_matrix_file = open("scoring_matrix.txt", 'r')
    except IOError:
        scoring_matrix_file = open("scoring_matrix.txt", "a")
        for row in range(nbRow):
            for col in range(nbCol):
                scoring_matrix_file.write(str(matrix[row][col]) + str(" "))
            scoring_matrix_file.write(str("\n"))
    finally:
        scoring_matrix_file.close()


def check_if_user_has_read_book(rank_book_read):
    '''
    This function will check if a user has Read a Book before allowing him to Rate it
    PARAMETERS:
        < rank_book_read >: The function takes in parameter an integer corresponding
        to the number of the book to check.

    RETURNS:
        < False >: The function return the boolean False if the user has not
        read the book
        < True >: The function return the boolean True if the user has read the book
    '''

    with open('booksread.txt', 'r', encoding='utf-8') as readers_file:
        rank_book_read = rank_book_read + 1
        rank_book_read = str(rank_book_read)
        readers_list = utility.remove_gap(readers_file.readlines())
        for reader in readers_list:
            split_reader = reader.split(',')
            for user_info in split_reader:
                if user_info == rank_book_read:
                    return True

        return False


def write_in_scoring_matrix(matrix_rows):
    '''
    This function overwrites the scoring matrix and re-writes it with the matrix_rows
    put as parameters

    PARAMETERS:
        < matrix_rows >: The function takes a matrix_rows as a parameter
        It's the content of that matrix_rows that will overwrite the file

    RETURNS:
        < Nothing >: The function doesn't return anything as it acts on the
        scoring_matrix_file
    '''

    with open('scoring_matrix.txt', 'w', encoding='utf-8') as scoring_matrix:
        for row in matrix_rows:
            scoring_matrix.write(row + "\n")


def rate_a_book():
    """
    PARAMETERS:
        < Nothing > : The function takes nothing in parameters since it ask pseudonym, name of the book to rate and
        its rate.
    RETURNS :
        < False > : The function return the boolean False if the user has not read the book .
        < True > : The function return the boolean True if the user has read the book ."""
    searched_reader = input("Enter a pseudonym : \n> ")
    # This variable does_reader_exist will either return False or the rank of the user if he exist
    does_reader_exist = get_user_index(searched_reader)
    if does_reader_exist == 'False' :
        print("The user that you searched doesn't exist.")
    else:
        book_to_search = input("Enter the name of the book that you want to rate :\n> ")
        # This variable check_if_book_exist... will either return False or the rank of the book if he exist
        if booksfunctions.get_book_index(book_to_search) is None:
            print("The book that you want to rate does not exist.")
        else:
            # Here we conserve the rank (in list language so rank - 1) of the book that we want to rate
            rank_of_book_to_rate = booksfunctions.get_book_index(book_to_search)
            print(rank_of_book_to_rate)
            # This function will check if the user entered has read the book and return either False or True
            if check_if_user_has_read_book(rank_of_book_to_rate):
                list_allowed_value = ['1', '2', '3', '4', '5']
                rate_given = input("Give a note to the selected book : (between 1 and 5)\n> ")
                # We check if the rate given is between 1 and 5 and if it's a single digit string
                while utility.is_string_correct_format(rate_given,list_allowed_value) == False or utility.more_than_1_char(rate_given) == True:
                    print("Value of rating not correct. Don't forget, you can only rate from 1 to 5.")
                    rate_given = input("Give a note to the selected book :\n> ")

                scoring_matrix = open("scoring_matrix.txt", "r")
                # Create a list and remove the \n in the new list that we created from the file
                lines_in_matrix = utility.remove_gap(scoring_matrix.readlines())
                scoring_matrix.close()
                # In does_reader_exist, we have the rank of the reader stored and therefore we split the line correspon
                # ding to the books that he has read in the lines_in_matrix list
                we_split_the_reader_line = lines_in_matrix[does_reader_exist].split(" ")
                rank_of_book_to_rate = int(rank_of_book_to_rate)
                # We browse the books that the user has read
                for book in range(len(we_split_the_reader_line)):
                    # we searched the moment where the book to rate is equal to the book in the depository
                    if book == rank_of_book_to_rate:
                        # we give the rate to the correct book
                        we_split_the_reader_line[book] = rate_given
                # we transform our list into a normal string separated by spaces
                we_split_the_reader_line = " ".join(we_split_the_reader_line)
                lines_in_matrix[does_reader_exist] = we_split_the_reader_line
                # we then re-write the scoring matrix file with the added rate
                write_in_scoring_matrix(lines_in_matrix)
            else:
                print("The user has not read the book that you want to rate.")


def book_not_read(user_looking4books, user2):
    '''
    The function takes in parameters two user's numbers, and returns a list of all the book's number that user 1
    didn't read compare to user 2
    PARAMETERS:
        < user_looking4books >: First user (Integer).
        < user2 > Second user (Integer)
        RETURNS:
                < list_to_return >: The function returns the list storing all the books not read by user_looking4books, but by user2
    '''

    with open("booksread.txt", "r") as read_books:
        books_r = read_books.readlines()
        list_to_return = []
        for i in range(len(books_r)):
            books_r[i] = books_r[i].rstrip("\n")
        book_user1 = books_r[user_looking4books].split(",")
        book_user2 = books_r[user2].split(",")
        book_user2.pop(0)
        for i in book_user2:
            if i not in book_user1:
                list_to_return.append(i)
        return list_to_return


def recommendation_possible(list_of_books):
    '''
    The function takes a list and return True is it is not empty
    PARAMETERS:
        < list_of_books >: Can be None or a list .
        RETURNS:
            < True >: True boolean if the list is not empty
            < False >: False boolean if the list is empty
    '''

    if list_of_books == None or len(list_of_books) == 0:
        return False
    return True


def books_to_recommend(list_of_books):
    '''
    The function prints a list a book to recommend from book_not_read
    PARAMETERS:
        < list_of_books >: Can be None or a list
        RETURNS:
            < True >: True boolean if the list is not empty
            < False >: False boolean if the list is empty
    '''

    with open("books.txt", "r") as fbooks:
        books = fbooks.readlines()
        list = []
        for i in list_of_books:
            list.append(books[int(i)].rstrip("\n"))
        print("""We recommend you these book(s) : """, list)
        return True  # We return True so that it doesn't print None


def same_book_read_and_rated(user1, user2):
    '''
    The function takes in parameters two number corresponding to two users and 
    returns a list in which there is thenumber of each book bot users have read add rate.

    PARAMETERS:
        < user1 >: Integer corresponding to the index of the first user
        < user2 >: Integer corresponding to the index of the second user

    RETURNS:
        < list_return >: List storing the number of the book that at least one 
        of the users as rate
    '''

    with open("booksread.txt", "r") as read_books, open("scoring_matrix.txt", "r") as rates_of_books:
        books_r = read_books.readlines()  # For example : ['Jade,0,1,4\n', 'Lionel,0,2,4\n']
        rate_b = rates_of_books.readlines()  # For example : ['4 3 0 0 5 0\n', '5 0 4 0 4 0'\n']
        for i in range(len(books_r)):
            books_r[i] = books_r[i].rstrip("\n")  # We delete "\n" from the variable
        for i in range(len(rate_b)):
            rate_b[i] = rate_b[i].rstrip("\n")  # We delete "\n" from the variable
        rate_b_user1 = cut_space_from_list(transform_str_list(rate_b[user1]))  # We delete all spaces from the variable and transform it into a list
        rate_b_user2 = cut_space_from_list(transform_str_list(rate_b[user2]))  # For example ['4','3','0','0','5','0']
        list_return = []
        for i in range(len(rate_b_user2)):
            if int(rate_b_user2[i]) != 0 or int(rate_b_user1[i]) != 0:  # We check if at least one of the two user read the book
                list_return.append(i)
        return list_return


def cut_space_from_list(list):
    '''
    This function take in parameters a list and deletes one element over 2 of this 
    list and returns it. Here it is only used for deleting '' from list with 
    one over two '' in it.

    PARAMETERS:
        < list >: List with a space in a element over two

    RETURNS:
        < list >: List without the spaces (one element over two have been deleted)
    '''

    x = len(list) // 2
    for i in range(x):
        list.pop(-2 - i)
    return list


def transform_str_list(input_str):
    '''
    The function takes in parameter a str and returns a list with each element
    of the string and delete '\n' and takes out spaces

    PARAMETERS:
        < input_str >: String

    RETURNS:
        < tab >: List storing all the elements one by one from the string
    '''

    tab = []
    for i in input_str:
        tab.append(i)
    for i in range(len(tab)):
        tab[i] = tab[i].rstrip("\n")
    return tab


def create_similarity_matrix():
    ''' 
    The function create returns the similarity matrix filled of 0

    PARAMETERS:
        < Nothing >: The function doesn't need anything to build the 
        matrix since it uses the 'readers.txt' file.

    RETURNS:
        < similarity_matrix >: matrix filled of 0, of length number_readers
    '''

    with open("readers.txt", "r") as readers_list:
        number_readers = len(readers_list.readlines())
        similarity_matrix = [[0 for i in range(number_readers)] for y in range(number_readers)]
        return similarity_matrix  # For example [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


def calculation_between_2_users(user1, user2, rates1, rates2):
    '''
    The function takes in parameters two user's number and their rates of each books. 
    Then it returns their proximity

    PARAMETERS:
        < user1 >: Integer corresponding to the index of the first user
        < user2 >: Integer corresponding to the index of the second user
        < rates1 >: List of string of user1's ratings
        < rates2 >: List of string of user2's ratings

    RETURNS:
        < 0 >: The function returns of if the denominator or the numerator is 0
        < round(sum_ab / (math.sqrt(sum_a2) * math.sqrt(sum_b2)), 2) >: The result of the formula 
        rounded at 2 number after the comma
    '''

    x = y = z = 0
    list_book_read = same_book_read_and_rated(user1, user2)
    for i in list_book_read:
        x += (int(rates2[int(i)])) * (int(rates1[int(i)]))
        y += int((rates1[int(i)])) ** 2
        z += int(rates2[int(i)]) ** 2
    if y == 0 or z == 0 or x == 0:
        return 0  # We cannot make division by 0, that's why we return 0 if the denominator is 0
    return round(x / (math.sqrt(y) * math.sqrt(z)), 2)  # We return the recommendation note


def Cosine_Similarity(user_1, user_2):
    '''
    The function takes in parameters two user's number and call 
    calculation_between_2_users of with the users and their book's rates, and returns it

    PARAMETERS:
        < user_1 >: Integer, first user .
        < user_2 >: Integer, second user .
    RETURNS:
        < calculation_between_2_users(user_1, user_2, rates_user1, rates_user2) >: Recommendation rate between
        user_1 and user_2
    '''

    with open("scoring_matrix.txt", "r") as score_matrix:
        users_rates = score_matrix.readlines()
        rates_user1, rates_user2 = users_rates[user_1], users_rates[user_2]
        rates_user1 = rates_user1.replace("\n", "")
        rates_user2 = rates_user2.replace("\n", "")
        rates_user1 = rates_user1.split(" ")
        rates_user2 = rates_user2.split(" ")
        # We delete all spaces and "\n"
        return calculation_between_2_users(user_1, user_2, rates_user1, rates_user2)


def simliraty():
    '''
        The Function defines the proximity between all users and fill the matrix with it, then returns it

    PARAMETERS:
        < Nothing >: The function doesn't need any parameters
        RETURNS:
            < sim_matrix >: Matrix filled with the recommend rate 
    '''

    sim_matrix = create_similarity_matrix()
    for i in range(len(sim_matrix)):
        for j in range(len(sim_matrix)):
            sim_matrix[i][j] = Cosine_Similarity(i,
                                                 j)  # We fill each place in the matrix by the recommendation note between two users
    return sim_matrix


def most_similar(name_of_user):
    '''
    The function takes in parameter a user's number and returns an other user's number. This one is the most similar
    one due to the algorithm.

    PARAMETERS:
        < name_of_user >: User's number, integer
        RETURNS:
            < maxi >: User number that is the closest to name_of_user in the recommendation matrix '''

    x = 0
    maxi = 0
    max_valor = 0
    for a in simliraty()[name_of_user]:
        if a > max_valor and name_of_user != x:  # We check if there is a variable greater than the last one and exclude the case of comparing to itself
            max_valor = a
            maxi = x
        x += 1
    return maxi


def recommend_book():
    '''
    The function prints if it can recommend book to the user or not

    PARAMETERS:
        < Nothing >: The function takes nothing in parameters
        RETURNS:
            < Nothing >: It's the menu of recommend book, it makes print which book to recommend you 
    '''

    name_user = input("Enter a pseudonym : \n> ")
    # This variable does_reader_exist will either return False or the rank of the user if he exist
    does_reader_exist = get_user_index(name_user)
    if does_reader_exist is False:
        print("The user that you searched doesn't exist.")
    else:
        if not recommendation_possible(book_not_read(does_reader_exist, most_similar(does_reader_exist))):
            print("""We don't have yet any recommendation for you !""")
        else:
            books_to_recommend(book_not_read(does_reader_exist, most_similar(does_reader_exist)))
        return True  # We return True so that it doesn't print None
