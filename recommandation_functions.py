# ------------------ RECOMMENDATION BOOK FUNCTIONS ---------------
import readers_functions as readersfunctions
from books_functions import *


# Function to create the scoring matrix that will be initaliazed the first time that the program will be launched
# It will write/create a scoring matrix file whenever it doesn't exists to conserve the data.

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


def check_if_user_read_book(rank_book_read):
    with open("booksread.txt", "r") as readers_file:
        rank_book_read = rank_book_read + 1
        rank_book_read = str(rank_book_read)
        readers_list = remove_jump_of_line_in_list(readers_file.readlines())
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


def recommendation_menu():
    print("""You are currently are on the "RRecommendation" page. What do you want to do ?
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
        pass
    else:
        utility.launching_menu()
