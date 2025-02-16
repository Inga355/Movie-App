import json

# Name der JSON-Datei
FILENAME = 'movies.json'


def get_movies():
    """
    Returns a dictionary of lists that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open(FILENAME, 'r') as json_file:
            movies = json.load(json_file)
        return movies
    except FileNotFoundError:
        return {}


def save_movies(movies):
    """
    Gets all movies as an argument and saves them to the JSON file.
    """
    with open(FILENAME, 'w') as json_file:
        json.dump(movies, json_file, indent=4)
    print(f"Movies data has been saved to {FILENAME}")


def list_movies():
    """
    Prints a list of all movies and their details.
    """
    movies = get_movies()
    total_movies = len(movies)
    print("")
    print(f"{total_movies} movies in total")
    print("")
    for key, value in movies.items():
        print(f"{key} ({value[1]}): {value[0]}")


def add_movie():
    """
    Gets input from User for adding a new movie to the dictionary
    and saves the data in JSON file
    """
    movies = get_movies()
    title = input("Please enter a movie name: ")
    rating = float(input("Please enter the movie's rating: "))
    year = int(input("Please enter the year of release: "))
    movies[title] = [rating, year]
    save_movies(movies)
    print(f"The movie '{title}' has been added to the database.")


def delete_movie():
    """
    Gets user input and deletes movie from the dictionary.
    """
    movies = get_movies()
    title = input("Please enter the name of the movie you want to delete: ")
    if title in movies:
        del movies[title]
        save_movies(movies)
        print(f"The movie '{title}' has been deleted from the database.")
    else:
        print(f"ERROR! The movie '{title}' does not exist in the database.")


def update_movie_in_storage(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie
    and saves it.
    """
    movies = get_movies()
    if title in movies:
        movies[title][0] = rating
        save_movies(movies)
        print(f"The movie '{title}' has been updated with a new rating.")
    else:
        print(f"ERROR! The movie '{title}' does not exist in the database.")
