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

                # ARTIST CREATION: Extracting genre
                inputGenre = ""
                while len(inputGenre) == 0:
                    inputGenreName = input("Enter the name of the artist's main genre: ")
                    if len(inputGenre) == 0:
                        print("Invalid input. Please enter again.")

                cursor.execute("SELECT id FROM Genre WHERE name = :bindGenre", {"bindGenre": inputGenre})
                result = cursor.fetchone()

                # GENRE CREATION: Genre is UNKNOWN. Start genre creation
                if result == None:
                    
                    try:
                        yesNoGenre = int(input(
                            "Genre "+inputGenre+" not found. "
                            "Would you like to insert it into the database? "
                            "1 for yes, anything else to quit."
                        ))

                        # GENRE CREATION: If it does not exist in Genre -> Create new genre
                        if yesNoGenre == 1:

                            inputParentGenre =  ""
                            while len(inputParentGenre) == 0:
                                inputParentGenre = input("Enter the name of the genre's parent genre: ")
                                if len(inputParentGenre) == 0:
                                    print("Invalid input. Please enter again.")

                            cursor.execute("SELECT * FROM Parent_Genre WHERE name = :bindParent", {"bindParent", inputParentGenre})
                            result = cursor.fetchone()

                            # PARENT GENRE START
                            if result == None:

                                try:
                                    yesNoParentGenre = int(input(
                                        "Parent genre "+inputParentGenre+" "
                                        "not found. Would you like to insert it into the database? "
                                        "1 for yes, anything else to quit."
                                    ))

                                    # PARENT GENRE CREATION: Select root genre
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

                                                # If root genre not present, stay in loop
                                                if result == None:
                                                    print("Root genre is not in the database. Please select again")

                                                # Success: root genre is present
                                                else: 
                                                    # root_genre_id stored in rootGenreId
                                                    rootGenreId = result[0]
                                                    rootGenreLock = 1

                                    # PARENT GENRE CREATION: Exit via "any other number"
                                    else:
                                        raise SystemExit
                                    
                                    # PARENT GENRE CREATION: Insert into parent genre with data
                                    # rootGenreId, inputParentGenre
                                    print("Inserting parent genre " +inputParentGenre+" into database...")
                                    cursor.execute("INSERT INTO Parent_genre (name, root_genre_id) VALUES (:bindParentGenre, :bindRootId)", 
                                                   {"bindParentGenre": inputParentGenre, "bindRootId": rootGenreId})
                                    print(inputParentGenre+" is now in the database!")
                                    
                                    # PARENT GENRE CREATION: Extract parent genre id for genre
                                    cursor.execute("SELECT id FROM Parent_genre WHERE name = :bindParentName", {"bindParentName": inputParentGenre})
                                    result = cursor.fetchone()
                                    parentGenreId = result[0]

                                # PARENT GENRE CREATION: Exit via invalid input
                                except ValueError as e:
                                    raise SystemExit
                            
                            # GENRE CREATION: If parent genre DOES exist, extract parent_genre_id
                            else:
                                parentGenreId = result[0]
                            
                            # GENRE CREATION: INSERTION INTO GENRE
                            # Add genre with parentGenreId data, either created one or already existing one.

                            print()
                            print("Inserting genre " +inputGenre+ " into the database...")
                            cursor.execute("INSERT INTO Genre (name, parent_genre_id) VALUES (:bindName, :bindParentId)", 
                                           {"bindName": inputGenre, "bindParentId": parentGenreId})
                            print(inputGenre+" is now in the database!")
                            
                            # Extracting genre_id for artist insertion
                            cursor.execute("SELECT id FROM Genre WHERE name = :bindGenre", {"bindGenre": inputGenre})
                            result = cursor.fetchone()
                            genreId = result[0]

                        # GENRE CREATION: Exit via "any other number"
                        else:
                            raise SystemExit

                    # GENRE CREATION: Exit via invalid input
                    except ValueError as e:
                        raise SystemExit

                # GENRE CREATION: Genre is KNOWN. Extract genre_id for artist insertion
                else:
                    genreId = result[0]

                print(inputArtist+" marked as "+inputGenre)
                # Genre_id has been found, now start insertion process
                # variables: inputArtist, inputGenre, inputActive, inputDetails

                # ARTIST CREATION: Getting Active value (true or false)
                while(inputActive != 1 or inputActive != 2):
                    try: 
                        inputActive = int(input("Is "+inputArtist+" active? (1 for yes, 2 for no)"))
                        if(inputActive != 1 or inputActive !=2):
                            print("Invalid number, please enter again")
                    except ValueError as e:
                        print("Invalid input. Please enter again")

                if(inputActive == 1):
                    print(inputArtist+" marked as active")
                else:
                    print(inputArtist+" marked as inactive")

                # ARTIST CREATION: Getting details values (jsonb)
                # json data - sometimes unknown
                # city, country, continent, aka
                
                jsonLock = 0
                while(jsonLock == 0):
                    try:
                        cityYesNo = input("Is the city of the artist known? 1 for yes, any other number for no")

                        if(cityYesNo == 1):
                            
                            inputCity = ""
                            while(len(inputCity) == 0):
                                inputCity = input("What city is the artist from?")
                                if(len(inputCity) == 0):
                                    print("Invalid input. Please enter again.")
                        
                        countryYesNo = input("Is the country of the artist known? 1 for yes, any other number for no")

                        if(countryYesNo == 1):
                            inputCountry = ""
                            while(len(inputCountry) == 0):
                                inputCountry = input("What country is the artist from?")
                                if(len(inputCountry) == 0):
                                    print("Invalid input. Please enter again.")

                        continentYesNo = input("Is the continent of the artist known? 1 for yes, any other number for no")

                        if(continentYesNo == 1):
                            inputContinent = ""
                            while(len(inputContinent) == 0):
                                inputContinent = input("What continent is the artist from?")
                                if(len(inputContinent == 0)):
                                    print("Invalid input. Please enter again.")
                        
                        jsonLock = 1

                    except ValueError as e:
                        print("Invalid input. Please start over.")

                # ARTIST CREATION: Location json finished. Insert artist then ask about aka because that has to go infinite
                # inputArtist, inputGenre, inputActive, inputCity, inputCountry, inputContinent
                # For simplicity probably add artist then add details

                cursor.execute("INSERT INTO Artist (name, genre_id, active) VALUES" \
                "               (:bindArtist, :bindGenre, :bindActive)",
                                {"bindArtist": inputArtist, "bindGenre": inputGenre, "bindActive": inputActive})
                    

            # Ask for "aka" field for .json data. Keep asking until stop
            # Must be done with jsonb command, so do after artist insertion
            akaYesNo = input("Has the artist released music under another name? 1 for yes, any other number for no")

            if(akaYesNo == 1):
                inputAka = ""
                akaExit = 0
                while(len(inputAka) == 0 or akaExit == 0):
                    inputAka = input("What are their aliases?")




            # ARTIST CREATION: Exit via "any other number"
            else:
                raise SystemExit

        # ARTIST CREATION: Exit via invalid input
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