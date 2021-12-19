# ------------------ RECOMMENDATION BOOK FUNCTIONS ---------------
import readers_functions as readersfunctions
from books_functions import *
import utility_functions as utility

'''Function to create the scoring matrix that will be initaliazed the first time that the program will be launched
# It will write/create a scoring matrix file whenever it doesn't exists to conserve the data.'''


def create_scoring_matrix():
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


# Function that will check if the user has read a book, and returns
def check_if_user_read_book(rank_book_read):
    with open("booksread.txt", "r") as readers_file:
        rank_book_read = rank_book_read + 1
        rank_book_read = str(rank_book_read)
        readers_list = utility.remove_gap(readers_file.readlines())
        for reader in readers_list:
            split_reader = reader.split(",")
            for user_info in range(len(split_reader)):
                if split_reader[user_info] == rank_book_read:
                    return True
        return False


def write_in_scoring_matrix(list):
    scoring_matrix = open("scoring_matrix.txt", "w")
    scoring_matrix.close()
    scoring_matrix = open("scoring_matrix.txt", "a")
    for i in range(len(list)):
        scoring_matrix.write(str(list[i]))
        scoring_matrix.write(str("\n"))


def rate_a_book():
    searched_reader = input("Enter a pseudonym : \n> ")
    # This variable does_reader_exist will either return False or the rank of the user if he exist
    does_reader_exist = readersfunctions.check_if_user_already_exist_and_returns_rank(searched_reader)
    print(does_reader_exist)
    if not does_reader_exist:
        print("The user that you searched doesn't exist.")
    else:
        book_to_search = input("Enter the name of the book that you want to rate :\n> ")
        # This variable check_if_book_exist... will either return False or the rank of the book if he exist
        if not check_if_book_exist_then_returns_its_rank(book_to_search):
            print("The book that you want to rate does not exist.")
        else:
            # Here we conserve the rank (in list language so rank - 1) of the book that we want to rate
            rank_of_book_to_rate = check_if_book_exist_then_returns_its_rank(book_to_search)
            print(rank_of_book_to_rate)
            # This function will check if the user entered has read the book and return either False or True
            if check_if_user_read_book(rank_of_book_to_rate):
                list_allowed_value = ['1', '2', '3', '4', '5']
                rate_given = input("Give a note to the selected book : (between 1 and 5)\n> ")
                # We check if the rate given is between 1 and 5 and if it's a single digit string
                while utility.check_if_string_is_good(rate_given,
                                                      list_allowed_value) == False or utility.does_string_more_than_one_char(
                    rate_given) == True:
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

# ------------------ RECOMMENDATION BOOK FUNCTIONS ---------------
from books_functions import *
import math
# Function to create the scoring matrix that will be initaliazed the first time that the program will be launched
# It will write/create a scoring matrix file whenever it doesn't exists to conserve the data.

def create_scoring_matrix():
    """PARAMETERS:
        < Nothing > : The function doesn't need parameters for creating a scoring matrix since it opens book and reader
    files and use it for creating the matrix
        VARIABLES:
        < books_file > :  Name given to the "books.txt" file.
        < readers_file > :  Name given to the "readers.txt" file.
        < nbRow > : Integer of the length of readers_file.
        < nbCol > : Integer of the length of books_file.
        < matrix > : Matrix of nbRow rows and nbCol columns
        < scoring_matrix_file > File in which matrix is stored, with spaces between all variables.
       RETURNS :
        < Nothing > : The function instead creates a matrix in a file but returns nothing ."""
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

def check_if_user_already_exist_and_returns_rank(pseudo):
    """PARAMETERS:
            < pseudo > : String given corresponding to the name to look for.
        VARIABLES:
            < readers_list_checkers > :  Name given to the "readers.txt" file.
            < readers_in_list > : Stores readers_list_checkers in a list.
            < user > : Integer used for the loop (for user in range)
            < user_split > : Stores a matrix in which each new list correspond to an other profile.
            < rank > : Stores an integer corresponding to the user's profile place in the matrix.
        RETURNS :
            < False > : The function return the boolean False if the name isn't in readers file .
            < rank > : The function return a integer corresponding to the place of the pseudonym (pseudo) if the name
            is in readers file ."""
    with open("readers.txt", "r") as readers_list_checkers:
        readers_in_list = readers_list_checkers.readlines()
        for user in range(len(readers_in_list)):
            user_split = readers_in_list[user].split(",")
            if user_split[0] == pseudo:
                # The rank will return a value in the way of a list ("1" if the reader is the second, 0 if he's first..)
                rank = user
                return rank
    return False

def check_if_user_read_book(rank_book_read):
    """PARAMETERS:
                < rank_book_read > : The function takes in parameter an integer corresponding to the number of the
                book to check.
        VARIABLES:
                < readers_file > : Name given to "booksread.txt".
                < rank_book_read > : Becomes itself + 1 turned into a string
                < readers_in_list > : Stores readers_file without the '\n'in a list.
                < reader > : Integer used for the loop (for reader in range)
                < split_reader > : Stores a matrix in which each new list correspond to an other book's read profile.
                < user_info > : Integer used for the loop (for user_info in range)
        RETURNS :
                < False > : The function return the boolean False if the user has not read the book .
                < True > : The function return the boolean True if the user has read the book ."""
    with open("booksread.txt", "r") as readers_file:
        rank_book_read = rank_book_read + 1
        rank_book_read = str(rank_book_read)
        readers_list = utility.remove_gap(readers_file.readlines())
        for reader in readers_list:
            split_reader = reader.split(",")
            for user_info in range(len(split_reader)):
                if split_reader[user_info] == rank_book_read:
                    return True
        return False


def write_in_scoring_matrix(list):
    """PARAMETERS:
                < list > : The function takes in parameter a list.
        VARIABLES:
                < scoring_matrix > : Name given to "scoring_matrix.txt".
                < i > : Integer used for the loop (for i in range)
        RETURNS :
                < Nothing > : until it changes scoring_matrix """
    scoring_matrix = open("scoring_matrix.txt", "w")
    scoring_matrix.close()
    scoring_matrix = open("scoring_matrix.txt", "a")
    for i in range(len(list)):
        scoring_matrix.write(str(list[i]))
        scoring_matrix.write(str("\n"))


def rate_a_book():
    """PARAMETERS:
        < Nothing > : The function takes nothing in parameters since it ask pseudonym, name of the book to rate and
        its rate.
            VARIABLES:
                    < searched_reader > : String input corresponding to the profile to use.
                    < does_reader_exist > : Calls check_if_user_already_exist_and_returns_rank and is False if the user
            doesn't exist or an integer corresponding to its place in the readers file.





                    < readers_in_list > : Stores readers_file without the '\n'in a list.
                    < reader > : Integer used for the loop (for reader in range)
                    < split_reader > : Stores a matrix in which each new list correspond to an other book's read profile.
                    < user_info > : Integer used for the loop (for user_info in range)
            RETURNS :
                    < False > : The function return the boolean False if the user has not read the book .
                    < True > : The function return the boolean True if the user has read the book ."""
    searched_reader = input("Enter a pseudonym : \n> ")
    # This variable does_reader_exist will either return False or the rank of the user if he exist
    does_reader_exist = check_if_user_already_exist_and_returns_rank(searched_reader)
    print(does_reader_exist)
    if not does_reader_exist:
        print("The user that you searched doesn't exist.")
    else:
        book_to_search = input("Enter the name of the book that you want to rate :\n> ")
        # This variable check_if_book_exist... will either return False or the rank of the book if he exist
        if not check_if_book_exist_then_returns_its_rank(book_to_search):
            print("The book that you want to rate does not exist.")
        else:
            # Here we conserve the rank (in list language so rank - 1) of the book that we want to rate
            rank_of_book_to_rate = check_if_book_exist_then_returns_its_rank(book_to_search)
            print(rank_of_book_to_rate)
            # This function will check if the user entered has read the book and return either False or True
            if check_if_user_read_book(rank_of_book_to_rate):
                list_allowed_value = ['1', '2', '3', '4', '5']
                rate_given = input("Give a note to the selected book : (between 1 and 5)\n> ")
                # We check if the rate given is between 1 and 5 and if it's a single digit string
                while utility.check_if_string_is_good(rate_given,
                                                      list_allowed_value) == False or utility.does_string_more_than_one_char(
                        rate_given) == True:
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

def book_not_read(user_looking4books,user2):
    """The function takes in parameters two user's numbers, and returns a list of all the book's number that user 1
    didn't read compare to user 2"""
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
    """The function takes a list and return True is it is not empty"""
    if list_of_books == None or len(list_of_books)== 0:
        return False
    return True

def books_to_recommend(list_of_books):
    """The function prints a list a book to recommend from book_not_read """
    with open("books.txt", "r") as fbooks:
        books = fbooks.readlines()
        list = []
        for i in list_of_books:
            list.append(books[int(i)].rstrip("\n"))
        print("""We recommend you these book(s) : """, list)
        return True     # We return True so that it doesn't print None


def same_book_read_and_rated(user1,user2):
    """ The function takes in parameters two number corresponding to two users and returns a list in which there is the
     number of each book bot users have read add rate.
    """
    with open("booksread.txt", "r") as read_books, open("scoring_matrix.txt", "r") as rates_of_books:
        books_r = read_books.readlines()    # For example : ['Jade,0,1,4\n', 'Lionel,0,2,4\n']
        rate_b = rates_of_books.readlines()     # For example : ['4 3 0 0 5 0\n', '5 0 4 0 4 0'\n']
        for i in range(len(books_r)):
            books_r[i] = books_r[i].rstrip("\n")    # We delete "\n" from the variable
        for i in range(len(rate_b)):
            rate_b[i] = rate_b[i].rstrip("\n")  # We delete "\n" from the variable
        rate_b_user1 = cut_space_from_list(transform_str_list(rate_b[user1]))   # We delete all spaces from the variable and transform it into a list
        rate_b_user2 = cut_space_from_list(transform_str_list(rate_b[user2]))   # For example ['4','3','0','0','5','0']
        list_return = []
        for i in range(len(rate_b_user2)):
            if int(rate_b_user2[i]) != 0 or int(rate_b_user1[i]) != 0:  # We check if at least one of the two user read the book
                list_return.append(i)
        return list_return

def cut_space_from_list(list):
    """ This function take in parameters a list and deletes one element over 2 of this list and returns it. Here it is only used
    for deleting '' from list with one over two '' in it."""
    x = len(list)//2
    for i in range(x):
        list.pop(-2-i)
    return list


def transform_str_list(input_str):
    """The function takes in parameter a str and returns a list with each element of the string and delete "\n"
    and takes out spaces """
    tab=[]
    for i in input_str:
        tab.append(i)
    for i in range(len(tab)):
        tab[i] = tab[i].rstrip("\n")
    return tab

def create_similarity_matrix():
    """ The function create returns the similarity matrix filled of 0"""
    with open("readers.txt", "r") as readers_list:
        number_readers = len(readers_list.readlines())
        similarity_matrix =[[0 for i in range(number_readers)] for y in range(number_readers)]
        return similarity_matrix    # For example [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]


def calculation_between_2_users(user1, user2, rates1, rates2):
    """ The function takes in parameters two user's number and their rates of each books. Then it returns their
    proximity"""
    x = y = z = 0
    list_book_read = same_book_read_and_rated(user1, user2)
    for i in list_book_read:
        x += (int(rates2[int(i)])) * (int(rates1[int(i)]))
        y += int((rates1[int(i)]))**2
        z += int(rates2[int(i)])**2
    if y == 0 or z == 0:
        return 0    # We cannot make division by 0, that's why we return 0 if the denominator is 0
    a = x/(math.sqrt(y)*math.sqrt(z))
    return round(x/(math.sqrt(y)*math.sqrt(z)),2)   # We return the recommendation note

def Cosine_Similarity(user_1, user_2):
    """ The function takes in parameters two user's number and call calculation_between_2_users of with the users and
     their book's rates, and returns it"""
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
    """The Function defines the proximity between all users and fill the matrix with it, then returns it"""
    sim_matrix = create_similarity_matrix()
    for i in range(len(sim_matrix)):
        for j in range(len(sim_matrix)):
            sim_matrix[i][j] = Cosine_Similarity(i, j)  # We fill each place in the matrix by the recommendation note between two users
    return sim_matrix


def most_similar(name_of_user):
    """The function takes in parameter a user's number and returns an other user's number. This one is the most similar
    one due to the algorithm."""
    x = 0
    maxi = 0
    max_valor=0
    for a in simliraty()[name_of_user]:
        if a > max_valor and name_of_user != x: # We check if there is a variable greater than the last one and exclude the case of comparing to itself
            max_valor = a
            maxi = x
        x += 1
    return maxi



def recommend_book():
    """The function prints if it can recommend book to the user or not"""
    name_user = input("Enter a pseudonym : \n> ")
    # This variable does_reader_exist will either return False or the rank of the user if he exist
    does_reader_exist = check_if_user_already_exist_and_returns_rank(name_user)
    if does_reader_exist != False:
        print("The user that you searched doesn't exist.")
    else :
        if not recommendation_possible(book_not_read(does_reader_exist,most_similar(does_reader_exist))):
            print("""We don't have yet any recommendation for you !""")
        else:
            books_to_recommend(book_not_read(does_reader_exist,most_similar(does_reader_exist)))
        return True     # We return True so that it doesn't print None

