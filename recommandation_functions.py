from books_functions import *
from readers_functions import *
from pathlib import Path
from utilitary_functions import *
from os.path import exists as file_exists

# RECOMMENDATION FUNCTIONS

def initialize_2D_list(nbCol,nbRows):
    scoring_matrix_list = [[0] * nbCol] * nbRows
    return scoring_matrix_list

def create_scoring_matrix():
    with open("readers.txt", "r") as readers_list, open("books.txt", 'r') as books_list:
        nbRows = len(readers_list.readlines())
        nbCol = len(books_list.readlines())
        scoring_matrix = open("scoring_matrix.txt", "a")
        scoring_matrix_list = initialize_2D_list(nbCol,nbRows)
        write_in_scoring_matrix(scoring_matrix_list)

def write_in_scoring_matrix(matrix):
    with open("readers.txt", "r") as readers_list, open("books.txt", 'r') as books_list:
        nbRows = len(readers_list.readlines())
        nbCol = len(books_list.readlines())
    scoring_matrix = open("scoring_matrix.txt", "a")
    for i in range(nbRows):
        for j in range(nbCol):
            scoring_matrix.write(str(matrix[i][j]))
        scoring_matrix.write(str("\n"))
    scoring_matrix.close()

def check_if_user_read_book(rank_book_read):
    with open("booksread.txt","r") as readers_file :
        rank_book_read = rank_book_read + 1
        rank_book_read = str(rank_book_read)
        readers_list = remove_jump_of_line_in_list(readers_file.readlines())
        for reader in readers_list :
            split_reader = reader.split(",")
            for user_info in range(len(split_reader)) :
                if split_reader[user_info] == rank_book_read :
                    return True
        return False

# Global function that will check if a user exists in the readers.txt file plus return its position
def check_if_user_already_exist_and_returns_rank(pseudo):
    with open("readers.txt", "r") as readers_list_checkers:
        readers_in_list = readers_list_checkers.readlines()
        for user in range(len(readers_in_list)):
            user_split = readers_in_list[user].split(",")
            if user_split[0] == pseudo:
                # The rank will return a value in the way of a list ("1" if the reader is the second, 0 if he's first..)
                rank = user
                return rank
    return False

def rate_a_book():
    searched_reader = input("Enter a pseudonym : \n> ")
    # This variable does_reader_exist will either contain False or the rank of the user if he exist
    does_reader_exist = check_if_user_already_exist_and_returns_rank(searched_reader)
    print(does_reader_exist)
    if not does_reader_exist:
        print("The user that you searched doesn't exist.")
    else :
        book_to_search = input("Enter the name of the book that you want to rate :\n> ")
        if not check_if_book_exist_then_returns_its_rank(book_to_search):
            print("The book that you want to rate does not exist.")
        else:
            rank_of_book_to_rate = check_if_book_exist_then_returns_its_rank(book_to_search)
            print(rank_of_book_to_rate)
            if check_if_user_read_book(rank_of_book_to_rate):
                rate_given = int(input("Give a note to the selected book : (between 1 and 5)\n> "))
                while rate_given < 1 or rate_given > 5:
                    print("Value of rating not correct. Don't forget, you can only rate from 1 tO 5")
                    rate_given = int(input("Give a note to the selected book :\n> "))
                scoring_matrix = open("scoring_matrix.txt", "r")
                lines_in_matrix = scoring_matrix.readlines()
                scoring_matrix.close()
                we_split_the_reader_line = lines_in_matrix[does_reader_exist].split(",")
                rank_of_book_to_rate = str(rank_of_book_to_rate + 1)
                for i in range(len(we_split_the_reader_line)):
                    if we_split_the_reader_line[i] == rank_of_book_to_rate :
                        we_split_the_reader_line[i] = rate_given
                we_split_the_reader_line = "".join(we_split_the_reader_line)
                lines_in_matrix[does_reader_exist] = we_split_the_reader_line
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
        launching_menu()