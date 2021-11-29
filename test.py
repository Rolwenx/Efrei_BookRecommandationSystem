#file_test_appens = file_test = open("test.txt", "r")
#for line in file_test_appens:
 #   b = line.split(',')
 #   print(b)

def find_place_of_number(n, p):
    return n // 10**p % 10

def return_style_inverse_function(a):
    if a == 1:
        return "sci - fi"
    if a == 2:
        return 'Biography'
    if a == 3:
        return "Horror"
    if a == 4:
        return 'Romance'
    if a == 5:
        return 'Fable'
    if a == 6:
        return 'History'
    if a == 7:
        return 'Comedy'

def reading_style_reader_inverse_function(a):
    x=1
    b=a
    while b // 10 > 0:
        x=x+1
        b=b//10
    if x == 1 :
        return return_style_inverse_function(a)
    else:
        types = ''
        for i in range(x-1):
            types += str(return_style_inverse_function(find_place_of_number(a, i))), ','
        types += str(return_style_inverse_function(find_place_of_number(a, x)))
        return types

def reading_style_reader_function():
    print("""What type of books do you read ?
                1) sci-fi
                2) Biography
                3) Horror
                4) Romance
                5) Fable
                6) History
                7) Comedy
                8) Multiple choice
               """)
    reading_style_reader = int(input("Enter the corresponding number. You can choose multiple types by writing 8 \n> "))
    while reading_style_reader >8 or reading_style_reader <1 :
        reading_style_reader = int(input("""What type of books do you read ?
                        1) sci-fi
                        2) Biography
                        3) Horror
                        4) Romance
                        5) Fable
                        6) History
                        7) Comedy
                        8) Multiple choose
                       (Write the number corresponding to, you can choose multiple types by writing 8)\n"""))
    if reading_style_reader == 8:
        reading_style_reader=0
        tab_reading_style_reader = []
        while reading_style_reader!=8:
            reading_style_reader=int(input("""What type of books do you read ?
                    1) sci-fi
                    2) Biography
                    3) Horror
                    4) Romance
                    5) Fable
                    6) History
                    7) Comedy
                    8) Finish
                   (Write the number corresponding to, if you have finish choosing, write 8, you must choose at least one \n"""))
            while(reading_style_reader > 8 or reading_style_reader < 1) or (reading_style_reader == 8 and len(tab_reading_style_reader)==0):
                if len(tab_reading_style_reader)==0:
                    while len(tab_reading_style_reader)==0:
                        while reading_style_reader > 7 or reading_style_reader < 1:
                            reading_style_reader = int(input("""What type of books do you read ?
                                                                           1) sci-fi
                                                                           2) Biography
                                                                           3) Horror
                                                                           4) Romance
                                                                           5) Fable
                                                                           6) History
                                                                           7) Comedy
                                                                          (Write the number corresponding to, you must choose a least one ! \n"""))
                            tab_reading_style_reader.append(reading_style_reader)
                else:
                    while reading_style_reader > 8 or reading_style_reader < 1:
                        reading_style_reader = int(input("""What type of books do you read ?
                                        1) sci-fi
                                        2) Biography
                                        3) Horror
                                        4) Romance
                                        5) Fable
                                        6) History
                                        7) Comedy
                                        8) Finish
                                       (Write the number corresponding to, if you have finish choosing, write 8\n"""))
                    if reading_style_reader != 8:
                        if reading_style_reader not in tab_reading_style_reader:
                            tab_reading_style_reader.append(reading_style_reader)
            if reading_style_reader != 8:
                if reading_style_reader not in tab_reading_style_reader:
                    tab_reading_style_reader.append(reading_style_reader)
        return convert_list_to_chain(tab_reading_style_reader)
    return reading_style_reader


def adding_reader(file_readers_append):
    name_reader = name_reader_function()
    gender_reader = gender_reader_function()
    age_reader_category = age_reader_category_function(age_reader_function())
    reading_style_reader = reading_style_reader_function()
    file_readers_append.write(name_reader,gender_reader,age_reader_category,reading_style_reader,"\n")

def wiev_a_reader(reader_to_look_for,file_readers_read):
    for line in file_readers_read:
        b=line.split(',')
        if b[0]==reader_to_look_for:
            print('the reader has registered under the pseudonym ',b[0],', he is a ',gender_reader_inverse_function(b[1]),', ',age_reader_category_inverse_function(b[2]) 'and likes to read ',reading_style_reader_inverse_function(b[3]),' books')


#    actions = {1: lambda: (list_books(), reader_profiles_menu()), 2: lambda: (add_reader_profile(), reader_profiles_menu()), 3: reader_profiles_menu, 4: reader_profiles_menu, 5: reader_profiles_menu, 6: reader_profiles_menu}
#    if reader_profiles_menu_selection in actions:
#        actions[reader_profiles_menu_selection]()