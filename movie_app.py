import random
import os

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

    def _command_add_movie(self, title, rating, year, poster):
        """
        Adds a new movie to the database.
        :param title (str): The title of the movie.
        :param rating (float): The rating of the movie.
        :param year (int): The release year of the movie.
        :param poster (str): URL to OMDbAPI to display the poster image.
        """
        self._storage.add_movie(title, rating, year, poster)

    def _command_delete_movie(self, title):
        """
        Deletes a movie from the database.
        :param title (str): The title of the movie to delete.
        """
        self._storage.delete_movie(title)

    def _command_update_movie(self, title, rating):
        """
        Updates the rating of an existing movie.
        :param title (str): The title of the movie to update.
        :param rating (float): The new rating of the movie.
        """
        self._storage.update_movie(title, rating)

    def _command_movie_stats(self):
        """
        Displays statistics about the movies including average rating, median rating,
        best and worst movies.
        """
        movies = self._storage.get_movies()
        if not movies:
            print("No movies available yet. Please add movie.")

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
        movies = self._storage.get_movies()
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
        movies = self._storage.get_movies()
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
        movies = self._storage.get_movies()
        sorted_mov = sorted(movies.items(), key=lambda item: item[1][0], reverse=True)
        for movie, details in sorted_mov:
            print(f"{movie}: Rating: {details[0]}, Year: {details[1]}")


    def _command_generate_website(self):
        """
        Generates an HTML page displaying all movies using an external template.
        """
        movies = self._storage.get_movies()
        if not movies:
            print("No movies available to generate a website.")
            return

        # Load HTML template from file
        template_path = os.path.join("_static", "index_template.html")
        try:
            with open(template_path, "r", encoding="utf-8") as file:
                html_template = file.read()
        except FileNotFoundError:
            print(f"Error: Template file not found at {template_path}")
            return

        movie_grid_items = ""
        for title, details in movies.items():
            movie_grid_items += "<li class='movie'>"
            movie_grid_items += f"<img src='{details[2]}' alt='{title} poster' class='movie-poster'>"
            movie_grid_items += f"<div class='movie-title'>{title}</div>"
            movie_grid_items += f"<div class='movie-year'>{details[1]}</div>"
            movie_grid_items += f"<div class='movie-info'>Rating: {details[0]}</div>"
            movie_grid_items += "</li>"

        html_content = html_template.replace("{movie_grid}", movie_grid_items)

        with open("_static/index.html", "w", encoding="utf-8") as file:
            file.write(html_content)

        print("Website generated successfully: movies.html")


    def run(self):
        """
        Starts the application menu loop.
        """
        from main import print_menu, get_main_choice, handle_user_choice

        while True:
            print_menu()
            user_main_choice = get_main_choice()
            if user_main_choice == 0:
                print("Bye!")
                break
            handle_user_choice(user_main_choice, self)

