# Name: Jonathan Guadron
# Date: November 22, 2026
# Assignment: Module 6 - Movies: Table Queries
# Purpose: Connect to the movies database and display four query results.

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

# Read the database login from the local .env file.
secrets = dotenv_values(".env")

config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

db = None
cursor = None

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Query 1: Select all fields from the studio table.
    cursor.execute("SELECT * FROM studio ORDER BY studio_id")
    studios = cursor.fetchall()

    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(
            studio[0], studio[1]
        ))

    # Query 2: Select all fields from the genre table.
    cursor.execute("SELECT * FROM genre ORDER BY genre_id")
    genres = cursor.fetchall()

    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(
            genre[0], genre[1]
        ))

    # Query 3: Select films with runtimes under 120 minutes.
    cursor.execute(
        "SELECT film_name, film_runtime FROM film "
        "WHERE film_runtime < 120 ORDER BY film_id"
    )
    short_films = cursor.fetchall()

    print("\n-- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print("Film Name: {}\nRuntime: {}\n".format(
            film[0], film[1]
        ))

    # Query 4: Arrange films by director, then their original ID.
    cursor.execute(
        "SELECT film_name, film_director FROM film "
        "ORDER BY film_director, film_id"
    )
    director_films = cursor.fetchall()

    print("\n-- DISPLAYING Director RECORDS in Order --")
    for film in director_films:
        print("Film Name: {}\nDirector: {}\n".format(
            film[0], film[1]
        ))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    # Close resources only if they were created.
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()