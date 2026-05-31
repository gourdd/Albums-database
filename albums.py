# The albums database!!!!
# Bryan Yamsuan

import sqlite3
connection = sqlite3.connect('albums.db')
cursor = connection.cursor()

try:

    # First, ask for the artist name, store it in bindArtist
    inputArtist = ""
    while len(inputArtist) == 0:
        inputArtist = input("Type the artist of the album you would like to insert: ")
        if len(inputArtist) == 0:
            print("Invalid input. Please enter again")

    # Check if there is a tuple with the artist name in the Artist table
    cursor.execute("SELECT * FROM Artist WHERE name = :inputArtistBind", {"inputArtistBind": inputArtist})
    result = cursor.fetchone()

    # Artist unknown -> Create new artist
    if result == None:
        
        try:
            yesNoArtist = int(input("Artist "+inputArtist+" unknown. Would you like to insert them into the database? 1 for yes, anything else to quit "))

            if yesNoArtist == 1:

                # Creating new artist : Insert genre
                inputGenre = ""
                while len(inputGenre) == 0:
                    inputGenreName = input("Enter the name of the artist's main genre: ")
                    if len(inputGenre) == 0:
                        print("Invalid input. Please enter again")

                cursor.execute("SELECT * FROM Genre WHERE name = :inputGenreBind", {"inputGenreBind": inputGenre})
                result = cursor.fetchone()
                if result == None:
                    print("hi")
                else:


            else:
                raise SystemExit

        # If user inputs a non-integer, value error goes to SystemExit
        except ValueError as e:
            raise SystemExit

    # Artist known -> fetch artist_id from inputArtist name
    else:
        print("hi")


except SystemExit as se:
    print("You have quit the program. Have a good day")

except Exception as e:
    print(e)

finally:
    connection.close()