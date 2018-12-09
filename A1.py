"""
Student Name: Sai Aung Sein Lin
Student ID: 13576310
Date: 09/12/2018
This is the program to learn the song whether they are learned or not.
Github: https://github.com/alfiexian5687/assessment_1/blob/master/A1.py
"""

from operator import itemgetter  # import the itemgetter function from the operator
Filename = "songs.csv"  # import the song.csv function to the program


def main_menu():  # function that request the menu choice
    menu = "Menu:\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n>>> "  # Asking for menu input
    selection = input(menu).upper()  # Making the input into capital letters
    while selection not in list("LACQ"):
        print("Invalid choice")
        selection = input(menu).upper()  # Re-Asking for menu input
    return selection  # Return the menu input


"""
loading songs
    list_of_song = list
    in_file = open songs.csv (r)
    for line in in_file
        remove new character
        song_artist_year_list = split line for ","
        list_of_song = append song_artist_year_list
    return list_of_song
"""


def loaded_songs():  # function that open the songs file and imput them to song_list
    list_of_song = []
    in_file = open(Filename, 'r')  # "r" the meaning of read
    for line in in_file:  # loop
        line = line.strip("\n")  # to strip the line
        song_artist_year_list = line.split(",")  # to split the line to the datum list
        list_of_song.append(song_artist_year_list)
        # to save all the "song_artist_year_list" in file_list. inside file_list is the "song_artist_year_list (list)"
    in_file.close()
    return list_of_song


def display_song_list(list_of_song): # display_song_list function prints a formatted table of songs from song_list
    count = 0  # to declare the variable and start form 0
    for i in range(len(list_of_song)):  # make the constant "i"
        if list_of_song[i][3] == "y":  # make the program to count symbol"y" in the csv file
            count += 1                 # to make the counting
            symbol = "*"               # to add the * symbol beside the complete song list
        else:
            symbol = " "               # to add the blank  beside the incomplete song list
        print(" ", str(i) + ".", symbol, "", end= " ")  # to show the results of the list
        for j in range(len(list_of_song[i]) - 2):    # the ddlist of the song
            if j == 1:              # analysing the j
                dash = "-"  # adding the dash symbol
            else:
                dash = ""  # adding the blank symbol
            print(dash, "{:30}".format(list_of_song[i][j]), end= " ")
        print("({:5})".format(list_of_song[i][-2]))
    print(len(list_of_song) - count, "songs learned,", count, "songs still to learn")
    # to show the user the number of song that need to learn


"""
learned_song(list_of_song)
song_number = get_integer("song number: ")
song_list[song_number][3] = "n"
print song_list[song_number][0]+"by"+song_list[song_number][1]+"learned"
return song_list
"""


def learned_song(list_of_song):     # the function that mark the songs as complete
    count = 0  # to declare the variable and start form 0
    for i in range(len(list_of_song)):  # make the constant "i"
        if list_of_song[i][3] == "y":  # make the program to count symbol"y" in the csv file
            count += 1     # to make the counting
            symbol = "*"   # to add the * symbol beside the complete song list
        else:              # to add the blank  beside the incomplete song list
            symbol = " "   # to add the blank  beside the incomplete song list
        print(" ", str(i) + ".", symbol, "", end= " ")  # to show the results of the list
        for j in range(len(list_of_song[i]) - 2):  # the list of the song
            if j == 1:   # analysing the j
                dash = "-"  # adding the dash symbol
            else:
                dash = ""   # adding the blank symbol
            print(dash, "{:30}".format(list_of_song[i][j]), end= " ")
        print("({:4})".format(list_of_song[i][-2]))
    if count ==0:
        print("No song need to learn. Please kindly enter 2 and Q to Quit")

    print(len(list_of_song) - count, "songs learned,", count, "songs still to learn")  # to show the user the number of song that need to learn
    s_number = count_number("Enter the no. of the song that you want to learn\n>>> ")  # For the user to choose the number to learn with the song number
    if list_of_song[s_number][3] == "n":  # If there is "n" in forth position in csv file, it show the duplicate message
        print("You have already learned", list_of_song[s_number][0])
    else:
        list_of_song[s_number][3] = "n"  # If there is "n" but for the song that is not in th above if statement, there will be marked as learned
        print(list_of_song[s_number][0], "by", list_of_song[s_number][1], "learned")
        return list_of_song


def input_word(prompt):   # to collecte the user input easily and th solve the error, i created the get_string functions
    string_input = input(prompt)  # to connect between the all user input prompt and string_input
    while len(string_input) == 0:  # when the user did not write anything, it will pop up the following message
        print("Input can not be blank")  # if the imput blank, it will shown "Input can not be blank"
        string_input = input(prompt)  # to re - request the prompt
    return string_input.title()  # to return to the string-input.title

def add_new_song():  # the function that add the new song to the songs.csv
    input_song = []
    title = input_word("Title: ")  # input the title
    artist = input_word("Artist: ")  # input the Artist
    year = str(count_year("Year: "))  # input the year
    input_song.append(title)  # add to the list add_new_song from the title_name
    input_song.append(artist)  # add to the list add_new_song from the artist_name
    input_song.append(year)  # add to the list add_new_song from the Year
    input_song.append("y")  # add to the list add_new_song from symbol "y"
    print(title, "by", artist, "({:5})".format(year), "added to song list")  # prompt that show user that the song has
    return input_song  # returned to input_song                                been added

def count_number(prompt):  # the function that control the number counting in the whole program
    valid = False       # to make variable as False
    while not valid:    # to make while loop
        try:
            input_number = int(input(prompt))  # make connection between the integer input and the
            if input_number < 0:            # if the user input is less than 0, it will show the error message.
                print("Number must be >= 0")  # the error message
            elif input_number >= 7:      # if the user input more than 7, it will show the following error message
                print("Song number is not in the list")  # the error message
            else:
                return input_number  # to make user to rewrite
        except ValueError:
            print("Invalid input; enter a valid number")


def count_year(prompt):
    valid = False       # to make variable as False
    while not valid:    # to make while loop
        try:
            input_number = int(input(prompt))  # make connection between the integer input and the
            if input_number < 0:            # if the user input is less than 0, it will show the error message.
                print("Number must be >= 0")  # the error message
            else:
                return input_number  # to make user to rewrite number
        except ValueError:  # for the value error
            print("The input is invalid; enter a valid number")


def saving_songs(list_of_song):   # function that save the song to list_of_song
    final_file = open(Filename, 'w')    # if the code is "w', it will overwrite the whole program in list
    for i in range(len(list_of_song)):  # the constant and the variable
        if i != 0:
            print("\n", end="", file= final_file)  # the  message that show th final file
        for j in range(len(list_of_song[i])):   # constant j is represent that range of the list
            final_file.write(list_of_song[i][j])  # write the arranged data into the songs.csv
            if j != 3:
                print(",", end="", file=final_file)  # the message that show the confidential note
    final_file.close()  # close the songs.csv file


def main():  # the main function
    print("Songs To Learn")
    Song_list = loaded_songs()  # to connect list_of_song function and loading song function
    print(len(Song_list), "Songs loaded")  # this function is to shows the number of songs contain in songs.csv
    menu_selection = main_menu()  # to connect menu_Selection and main_Menu()
    while menu_selection != "Q":  # If user enter Q, this will go to  Song_list.sort function
        Song_list.sort(key=itemgetter(1, 0))
        if menu_selection == "C":  # If user enter C, this will go to display_song_complete_a_song(Song_list)function
            learned_song(Song_list)
        elif menu_selection == "A":  # If user enter A, this will go to display_song_list(Song_list) function
            Song_list.append(add_new_song())
        else:  # If user enter L, this will go to display_song_list(Song_list) function
            display_song_list(Song_list)
        menu_selection = main_menu()  # to connected between menu_Selection and main_Menu()
    saving_songs(Song_list)  # If user enter Q, the program will overwrite the csv file
    print(len(Song_list), "Song has been saved to", Filename, "\nGood day, sir xD")  # Save tocsv and show farewell message


if __name__ == '__main__':
    main()

