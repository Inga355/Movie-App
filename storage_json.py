from istorage import IStorage
import json


def get_movies(filepath):
    """
    Returns a dictionary of lists that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open(filepath, 'r') as json_file:
            movies = json.load(json_file)
        return movies
    except FileNotFoundError:
        print('No data in database.')
        return {}


def save_movies(movies, filepath):
    """
    Gets all movies as an argument and saves them to the JSON file.
    """
    with open(filepath, 'w') as json_file:
        json.dump(movies, json_file, indent=4)
    print(f"Movies data has been saved to {filepath}")


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Prints a list of all movies in database and their details.
        """
        movies = get_movies(self.file_path)
        total_movies = len(movies)
        print("")
        print(f"{total_movies} movies in total")
        print("")
        for key, value in movies.items():
            print(f"{key} ({value[1]}): {value[0]}")


    def add_movie(self, title, year, rating):
        """
        Adds a movie to the movies database
        Loads the dictionary from the JSON, gets user input,
        adds the movie and saves it in JSON
        """
        movies = get_movies(self.file_path)
        movies[title] = [rating, year]
        save_movies(movies, self.file_path)
        print(f"The movie '{title}' has been added to the database.")


    def delete_movie(self, title):
        """
        Deletes a movie from the movies database
        Loads the dictionary from the JSON, gets user input,
        deletes the movie and saves it in JSON
        """
        movies = get_movies(self.file_path)
        if title in movies:
            del movies[title]
            save_movies(movies, self.file_path)
            print(f"The movie '{title}' has been deleted from the database.")
        else:
            print(f"ERROR! The movie '{title}' does not exist in the database.")


    def update_movie(self, title, rating):
        """
        Updates a movie from the movie database.
        Loads the dictionary from the JSON file, gets user input,
        updates the movie and saves it in JSON
        """
        movies = get_movies(self.file_path)
        if title in movies:
            movies[title][0] = rating
            save_movies(movies, self.file_path)
            print(f"The movie '{title}' has been updated with a new rating.")
        else:
            print(f"ERROR! The movie '{title}' does not exist in the database.")