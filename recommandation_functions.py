from utilitary_functions import *
from readers_functions import check_if_user_already_exist
from books_functions import check_if_book_exist_then_returns_its_rank

# RECOMMENDATION FUNCTIONS

def create_scoring_matrix():
    with open("readers.txt","r") as readers_list, open("books.txt",'r') as books_list:
        nbRows = len(readers_list.readlines())
        nbCol = len(books_list.readlines())
        scoring_matrix = [[0] * nbCol] * nbRows

# This function will ask the user to enter a pseudonym if it is not called from the add reader function.
# Checks whether the pseudonym exists in the "readers.txt" file
# sks the user to enter the title of the book he or she wishes to rate
# Checks if the title exists in the "books.txt" file. If so, it saves its rank.
# Checks the "booksread.txt" file to see if the reader has read the book.
# - If so, it allows him or her to rate the book, making sure that the rating is an integer between 1 and 5


def rate_a_book():
    searched_reader = input("Enter a pseudonym : \n> ")
    if check_if_user_already_exist(searched_reader):
        book_to_search = input("Enter the name of the book that you want to rate :\n> ")
        print(check_if_book_exist_then_returns_its_rank(book_to_search) == check_if_book_exist_then_returns_its_rank(book_to_search)[1])





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