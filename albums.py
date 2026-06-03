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
    cursor.execute("SELECT * FROM Artist WHERE name = :bindArtist", {"bindArtist": inputArtist})
    result = cursor.fetchone()

    # Artist unknown -> Create new artist
    if result == None:
        
        try:
            yesNoArtist = int(input(
                "Artist "+inputArtist+" not found. "
                "Would you like to insert them into the database? "
                "1 for yes, anything else to quit."
            ))

            if yesNoArtist == 1:

                # Creating new artist : Insert genre
                inputGenre = ""
                while len(inputGenre) == 0:
                    inputGenreName = input("Enter the name of the artist's main genre: ")
                    if len(inputGenre) == 0:
                        print("Invalid input. Please enter again.")

                cursor.execute("SELECT * FROM Genre WHERE name = :bindGenre", {"bindGenre": inputGenre})
                result = cursor.fetchone()

                # Genre does not exist in Genre -> Create new genre
                if result == None:
                    
                    try:
                        yesNoGenre = int(input(
                            "Genre "+inputGenre+" not found. "
                            "Would you like to insert it into the database? "
                            "1 for yes, anything else to quit."
                        ))

                        if yesNoGenre == 1:

                            inputParentGenre =  ""
                            while len(inputParentGenre) == 0:
                                inputParentGenre = input("Enter the name of the genre's parent genre: ")
                                if len(inputParentGenre) == 0:
                                    print("Invalid input. Please enter again.")

                            cursor.execute("SELECT * FROM Parent_Genre WHERE name = :bindParent", {"bindParent", inputParentGenre})
                            result = cursor.fetchone()

                            # Parent genre does not exist in Parent genre -> Create new parent genre
                            if result == None:

                                try:
                                    yesNoParentGenre = int(input(
                                        "Parent genre "+inputParentGenre+" "
                                        "not found. Would you like to insert it into the database? "
                                        "1 for yes, anything else to quit."
                                    ))

                                    # Assign root genre to parent genre
                                    if yesNoParentGenre == 1:
                                        
                                        # Displaying all root genres
                                        cursor.execute("SELECT name FROM Root_genre")
                                        rows = cursor.fetchall()
                                        for row in rows:
                                            print(row)

                                        # Selecting root genre
                                        inputRootGenre = ""
                                        rootGenreLock = 0
                                        while len(inputRootGenre) == 0 or rootGenreLock == 0:

                                            inputRootGenre = input("Enter a root genre from this list: ")
                                            if len(inputRootGenre) == 0:
                                                print("Invalid input. Please enter again.")
                                            else:
                                                cursor.execute("SELECT id FROM Root_Genre WHERE name = :bindRootGenre", 
                                                                {"bindRootGenre": inputRootGenre})
                                                result = cursor.fetchone()

                                                if result == None:
                                                    print("Root genre is not in the database. Please select again")
                                                else: # Success case
                                                    # root_genre_id stored in rootGenreId
                                                    rootGenreId = result[0]
                                                    rootGenreLock = 1
                                    else:
                                        raise SystemExit
                                    
                                    # Insert into Parent_genre
                                    # rootGenreId, inputParentGenre
                                    print("Inserting parent genre " +inputParentGenre+" into database...")
                                    cursor.execute("INSERT INTO Parent_genre (name, root_genre_id) VALUES (:bindParent, :bindRootId)", 
                                                   {"bindParent": inputParentGenre, "bindRootId": rootGenreId})
                                    
                                    # You need to get the parent genre id now
                                    cursor.execute("SELECT id FROM Parent_genre WHERE name = :bindParentName", {"bindParentName": inputParentGenre})
                                    result = cursor.fetchone()
                                    parentGenreId = result[0]

                                except ValueError as e:
                                    raise SystemExit
                                
                    except ValueError as e:
                        raise SystemExit


                else:
                    raise SystemExit


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