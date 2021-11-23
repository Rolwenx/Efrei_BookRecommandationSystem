#Projet Python Yoke Joseph BOOKS
def list_books():
    """Prints the list of the books preceded by the sequential number"""
    file_books_list = open("books.txt", "r")
    a = 1
    for line in file_books_list:
        print(a,') ',line,end='')
        a+=1
    file_books_list.close()
