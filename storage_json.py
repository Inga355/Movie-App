from istorage import IStorage
import json
from movie_storage import get_movies, save_movies


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        Prints a list of all movies in database and their details.
        """
        movies = get_movies()
        total_movies = len(movies)
        print("")
        print(f"{total_movies} movies in total")
        print("")
        for key, value in movies.items():
            print(f"{key} ({value[1]}): {value[0]}")


    def add_movie(self, title, year, rating, poster):
        movies = get_movies()
        title = input("Please enter a movie name: ")
        rating = float(input("Please enter the movie's rating: "))
        year = int(input("Please enter the year of release: "))
        movies[title] = [rating, year]
        json.dump(movies, json_file, indent=4)
        print(f"The movie '{title}' has been added to the database.")

    def delete_movie(self, title):
        ...

    def update_movie(self, title, rating):
        ...