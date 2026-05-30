# The albums database!!!!
# Bryan Yamsuan

import sqlite3
connection = sqlite3.connect('albums.db')
cursor = connection.cursor()

try:

    # First, ask for the artist name, store it in bindArtist
    bindArtist = print("Type the artist of the album you would like to insert: ")

    


except Exception as e:
    print(e)

finally:
    connection.close()