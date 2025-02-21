from istorage import IStorage
import json


def get_movies(filepath):
    """
    Loads and returns movie data from a JSON file.
    :param filepath (str): The path to the JSON file containing movie data.
    :returns dict: A dictionary containing movie titles as keys and lists with rating and year as values.
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
    Saves the given movie dictionary to a JSON file.
    :param movies (dict): The dictionary containing movie data.
    :param filepath (str): The path to the JSON file where data should be saved.
    """
    with open(filepath, 'w') as json_file:
        json.dump(movies, json_file, indent=4)
    print(f"Movies data has been saved to {filepath}")


class StorageJson(IStorage):
    def __init__(self, file_path):
        """
        Initializes StorageJson with a file path.
        :param file_path (str): The path to the JSON file used for storing movie data.
        """
        self.file_path = file_path

    def list_movies(self):
        """
        Prints a list of all movies in database along with their details.
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
        Adds a movie to the database and saves the updated data to the JSON file.
        :param title (str): The title of the movie.
        :param year (int): The release year of the movie.
        :param rating (float): The rating of the movie.
        """
        movies = get_movies(self.file_path)
        movies[title] = [rating, year]
        save_movies(movies, self.file_path)
        print(f"The movie '{title}' has been added to the database.")


    def delete_movie(self, title):
        """
        Deletes a movie from the database and saves the updated data.
        :param title (str): The title of the movie to delete.
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
        Updates the rating of a movie and saves the updated data.
        :param title (str): The title of the movie to update.
        :param rating (float): The new rating for the movie.
        """
        movies = get_movies(self.file_path)
        if title in movies:
            movies[title][0] = rating
            save_movies(movies, self.file_path)
            print(f"The movie '{title}' has been updated with a new rating.")
        else:
            print(f"ERROR! The movie '{title}' does not exist in the database.")