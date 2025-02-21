from storage_json import get_movies
import random


class MovieApp:
    def __init__(self, storage):
        """
        Initializes the MovieApp with a storage backend.
        :param storage (StorageJson): An instance of the storage class.
        """
        self._storage = storage


    def _command_list_movies(self):
        """
        Lists all movies stored in the database.
        """
        return self._storage.list_movies()

    def _command_add_movie(self, title, rating, year):
        """
        Adds a new movie to the database.
        :param title (str): The title of the movie.
        :param rating (float): The rating of the movie.
        :param year (int): The release year of the movie.
        """
        self._storage.add_movie(title, rating, year)

    def _command_delete_movie(self, title):
        """
        Deletes a movie from the database.
        :param title (str): The title of the movie to delete.
        """
        self._storage.delete_movie(title)

    def _command_update_movie(self, title, rating):
        """
        Updates the rating of a existing movie.
        :param title (str): The title of the movie to update.
        :param rating (float): The new rating of the movie.
        """
        self._storage.update_movie(title, rating)

    def _command_movie_stats(self):
        """
        Displays statistics about the movies including average rating, median rating,
        best and worst movies.
        """
        movies = get_movies(self._storage.file_path)
        print("")
        """Average rating"""
        average_rating = sum(movie[0] for movie in movies.values()) / len(movies)
        print(f"The average rating is: {average_rating}")

        """Median rating"""
        ratings = sorted(movie[0] for movie in movies.values())
        n = len(ratings)
        if n % 2 == 0:
            median = (ratings[n // 2 - 1] + ratings[n // 2]) / 2
        else:
            median = ratings[n // 2]
        print(f"The median rating is: {median}")

        """Best movie"""
        max_rating = max(movie[0] for movie in movies.values())
        top_movies = [movie for movie, details in movies.items() if details[0] == max_rating]
        print(f"The top movie(s) are {', '.join(top_movies)} with a rating of {max_rating}.")

        """Worst movie"""
        min_rating = min(movie[0] for movie in movies.values())
        worst_movies = [movie for movie, details in movies.items() if details[0] == min_rating]
        print(f"The worst movie(s) are {', '.join(worst_movies)} with a rating of {min_rating}.")


    def _command_random_choice(self):
        """
        Selects and displays a random movie from the database.
        """
        movies = get_movies(self._storage.file_path)
        keys_list = list(movies.keys())
        r_choice_name = random.choice(keys_list)
        r_choice_rating = movies[r_choice_name][0]
        r_choice_year = movies[r_choice_name][1]
        print(f"Your random choice is: '{r_choice_name}' from {r_choice_year}. It's rated with {r_choice_rating}.")


    def _command_search_movie(self, search_term):
        """
        Searches for movies that contain the given search term in their title.
        :param search_term (str): The search string to match against movie titles.
        """
        movies = get_movies(self._storage.file_path)
        search_term_lower = search_term.lower()
        search_result = [movie for movie in movies if search_term_lower in movie.lower()]
        if search_result:
            for movie in search_result:
                print(f"{movie},  Rating: {movies[movie][0]}, Year: {movies[movie][1]}")
        else:
            print("Movie not found")


    def _command_sorted_movies(self):
        """
        Displays the movies sorted by their rating.
        """
        movies = get_movies(self._storage.file_path)
        sorted_mov = sorted(movies.items(), key=lambda item: item[1][0], reverse=True)
        for movie, details in sorted_mov:
            print(f"{movie}: Rating: {details[0]}, Year: {details[1]}")


    def _generate_website(self):
        """
        Placeholder for future functionality to generate a website.
        """
        pass


    def run(self):
        """
       Placeholder method to start the application.
       """
        pass

