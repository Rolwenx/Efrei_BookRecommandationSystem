#Projet Python Yoke Joseph BOOKS
file_books_read = file_books = open("books.txt", "r")
def print_list_books(file_books_read):
    """Prints the list of the books preceded by the sequential number"""
    a = 1
    for line in file_books_read:
        print(a,') ',line,end='')
        a+=1
print_list_books(file_books_read)
file_books_read.close()