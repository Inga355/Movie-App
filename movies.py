import random
from movie_storage import get_movies, add_movie, list_movies


# Display Menue and handle User-Input
def print_menu():
    """
    Prints the main menu options.
    """
    print("")
    print("Menu:")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("")


def get_main_choice():
    """
    Prompts the user to enter a choice from the main menu.
    :return: int: The user's choice as an integer.
    """
    while True:
        try:
            user_main_choice = int(input("Enter choice (0-10): "))
            if 0 <= user_main_choice <= 10:
                return user_main_choice
            else:
                print("Please enter a number between 0 and 10!")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10!")


def handle_user_choice(choice, movie_dictionary):
    """
    Handles the user's choice from the main menu and calls the appropriate function.
    :param choice: (int): The user's menu choice.
    :param movie_dictionary: (dict): The dictionary containing movie data.
    """
    if choice == 1:
        list_movies()
    elif choice == 2:
        add_movie()
    elif choice == 3:
        delete_movie(movie_dictionary)
    elif choice == 4:
        update_movie(movie_dictionary)
    elif choice == 5:
        show_stats(movie_dictionary)
    elif choice == 6:
        random_choice(movie_dictionary)
    elif choice == 7:
        search_term = input("Enter a part of a movie name: ")
        search_movie(movie_dictionary, search_term)
    elif choice == 8:
        sorted_movies(movie_dictionary)
    else:
        print("Wrong number, please choose again!")


# Functions to handle User Choice



def delete_movie(movie_dictionary):
    """
    Deletes a movie from the dictionary.
    :param movie_dictionary: (dict) The dictionary containing movie data.
    """
    movie_name = input("Please enter the name of the movie you want to delete: ")
    movie_value = movie_dictionary.pop(movie_name, None)
    print(f"The movie '{movie_name}' was deleted.")
    if movie_value is None:
        print(f"ERROR! The movie '{movie_name}' does not exists!")


def update_movie(movie_dictionary):
    """
    Updates the details of an existing movie in the dictionary.
    :param movie_dictionary: (dict) The dictionary containing movie data.
    """
    movie_name = input("Which movie do you want to update? Please enter the name: ")
    if movie_name in movie_dictionary:
        new_rating = float(input("Please enter the new rating: "))
        new_year = int(input("Please enter the new year of release: "))
        movie_dictionary[movie_name] = [new_rating, new_year]
        print(f"The movie '{movie_name}' was updated.")
    else:
        print(f"ERROR! The movie '{movie_name}' does not exists!")


def show_stats(movie_dictionary):
    """
    Displays statistics about the movies.
    :param movie_dictionary: (dict) The dictionary containing movie data.
    """
    print("")
    """Average rating"""
    average_rating = sum(movie[0] for movie in movie_dictionary.values()) / len(movie_dictionary)
    print(f"The average rating is: {average_rating}")

    """Median rating"""
    ratings = sorted(movie[0] for movie in movie_dictionary.values())
    n = len(ratings)
    if n % 2 == 0:
        median = (ratings[n // 2 - 1] + ratings[n // 2]) / 2
    else:
        median = ratings[n // 2]
    print(f"The median rating is: {median}")

    """Best movie"""
    max_rating = max(movie[0] for movie in movie_dictionary.values())
    top_movies = [movie for movie, details in movie_dictionary.items() if details[0] == max_rating]
    print(f"The top movie(s) are {', '.join(top_movies)} with a rating of {max_rating}.")

    """Worst movie"""
    min_rating = min(movie[0] for movie in movie_dictionary.values())
    worst_movies = [movie for movie, details in movie_dictionary.items() if details[0] == min_rating]
    print(f"The worst movie(s) are {', '.join(worst_movies)} with a rating of {min_rating}.")


def random_choice(movie_dictionary):
    """
    Selects a random movie from the dictionary and displays its details.
    :param movie_dictionary: (dict) The dictionary containing movie data.
    """
    keys_list = list(movie_dictionary.keys())
    r_choice_name = random.choice(keys_list)
    r_choice_rating = movie_dictionary[r_choice_name][0]
    r_choice_year = movie_dictionary[r_choice_name][1]
    print(f"Your random choice is: '{r_choice_name}' from {r_choice_year}. It's rated with {r_choice_rating}.")


def search_movie(movie_dictionary, search_term):
    """
    Searches for movies that contain the given search term in their title.
    :param movie_dictionary: (dict) The dictionary containing movie data.
    :param search_term: (str) The term to search for in movie titles.
    """
    search_term_lower = search_term.lower()
    search_result = [movie for movie in movie_dictionary if search_term_lower in movie.lower()]
    if search_result:
        for movie in search_result:
            print(f"{movie},  Rating: {movie_dictionary[movie][0]}, Year: {movie_dictionary[movie][1]}")
    else:
        print("Movie not found")


def sorted_movies(movie_dictionary):
    """
    Displays the movies sorted by their rating.
    :param movie_dictionary: (dict) The dictionary containing movie data.
    """
    sorted_mov = sorted(movie_dictionary.items(), key=lambda item: item[1][0], reverse=True)
    for movie, details in sorted_mov:
        print(f"{movie}: Rating: {details[0]}, Year: {details[1]}")


# Main Function
def main():
    """
    Main function that initializes the movie database and starts the menu loop.
    """
    movies = get_movies()

    print("********** My Movies Database **********")

    while True:
        print_menu()
        user_main_choice = get_main_choice()
        if user_main_choice == 0:
            print("Bye!")
            break
        handle_user_choice(user_main_choice, movies)


if __name__ == "__main__":
    main()
