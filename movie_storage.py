import json

# Name der JSON-Datei
FILENAME = 'movies.json'

def get_movies():
    """
    Returns a dictionary of dictionaries that
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
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(FILENAME, 'w') as json_file:
        json.dump(movies, json_file, indent=4)
    print(f"Movies data has been saved to {FILENAME}")

def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movies[title] = [rating, year]
    save_movies(movies)
    print(f"The movie '{title}' has been added to the database.")

def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if title in movies:
        del movies[title]
        save_movies(movies)
        print(f"The movie '{title}' has been deleted from the database.")
    else:
        print(f"ERROR! The movie '{title}' does not exist in the database.")

def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if title in movies:
        movies[title][0] = rating
        save_movies(movies)
        print(f"The movie '{title}' has been updated with a new rating.")
    else:
        print(f"ERROR! The movie '{title}' does not exist in the database.")
