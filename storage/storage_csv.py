import csv
from storage.istorage import IStorage


class StorageCsv(IStorage):
    """
    A storage implementation that saves movie data in a CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes the CSV storage with a file path.
        :param: file_path (str) The path to the CSV file used for storing movie data.
        """
        self.file_path = file_path

    def get_movies(self):
        """
        Loads movies from the CSV file and returns them as a dictionary.
        :returns: dict: A dictionary containing movie titles as keys and lists with rating and year as values.
        """
        movies = {}
        try:
            with open(self.file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:
                        title, rating, year, poster = row
                        movies[title] = [float(rating), int(year), str(poster)]
        except FileNotFoundError:
            print("No data in database.")
        return movies

    def save_movies(self, movies):
        """
        Saves the given movie dictionary to a CSV file.
        :param: movies (dict) The dictionary containing movie data.
        """
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for title, details in movies.items():
                writer.writerow([title, details[0], details[1], details[2]])
        print(f"Movies data has been saved to {self.file_path}")

    def list_movies(self):
        """
        Prints a list of all movies in the database along with their details.
        """
        movies = self.get_movies()
        total_movies = len(movies)
        print(f"\n{total_movies} movies in total\n")
        for key, value in movies.items():
            print(f"{key} ({value[1]}): {value[0]}")

    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the database and saves the updated data to the CSV file.

        :param: title (str) he title of the movie.
        :param: year (int) The release year of the movie.
        :param: rating (float) The rating of the movie.
        """
        movies = self.get_movies()
        movies[title] = [rating, year, poster]
        self.save_movies(movies)
        print(f"The movie '{title}' has been added to the database.")

    def delete_movie(self, title):
        """
        Deletes a movie from the database and saves the updated data.
        :param: title (str) The title of the movie to delete.
        """
        movies = self.get_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)
            print(f"The movie '{title}' has been deleted from the database.")
        else:
            print(f"ERROR! The movie '{title}' does not exist in the database.")

    def update_movie(self, title, rating):
        """
        Updates the rating of a movie and saves the updated data.
        :param: title (str) The title of the movie to update.
        :param: rating (float) The new rating for the movie.
        """
        movies = self.get_movies()
        if title in movies:
            movies[title][0] = rating
            self.save_movies(movies)
            print(f"The movie '{title}' has been updated with a new rating.")
        else:
            print(f"ERROR! The movie '{title}' does not exist in the database.")
