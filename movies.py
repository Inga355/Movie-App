import random
from movie_storage import get_movies, add_movie, list_movies, delete_movie, update_movie


# Display Menu and handle User-Input
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


def handle_user_choice(choice):
    """
    Handles the user's choice from the main menu and calls the appropriate function.
    :param choice: (int): The user's menu choice.
    """
    if choice == 1:
        list_movies()
    elif choice == 2:
        title = input("Please enter a movie name: ")
        rating = float(input("Please enter the movie's rating: "))
        year = int(input("Please enter the year of release: "))
        add_movie(title, rating, year)
    elif choice == 3:
        delete_movie()
    elif choice == 4:
        update_movie()
    elif choice == 5:
        show_stats()
    elif choice == 6:
        random_choice()
    elif choice == 7:
        search_movie()
    elif choice == 8:
        sorted_movies()
    else:
        print("Wrong number, please choose again!")


# Functions to analyse stats and providing infos on stored movies
def show_stats():
    """
    Displays statistics about the movies.
    """
    movies = get_movies()
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


def random_choice():
    """
    Selects a random movie from the dictionary and displays its details.
    """
    movies = get_movies()
    keys_list = list(movies.keys())
    r_choice_name = random.choice(keys_list)
    r_choice_rating = movies[r_choice_name][0]
    r_choice_year = movies[r_choice_name][1]
    print(f"Your random choice is: '{r_choice_name}' from {r_choice_year}. It's rated with {r_choice_rating}.")


def search_movie():
    """
    Searches for movies that contain the given search term in their title.
    """
    movies = get_movies()
    search_term = input("Enter a part of a movie name: ")
    search_term_lower = search_term.lower()
    search_result = [movie for movie in movies if search_term_lower in movie.lower()]
    if search_result:
        for movie in search_result:
            print(f"{movie},  Rating: {movies[movie][0]}, Year: {movies[movie][1]}")
    else:
        print("Movie not found")


def sorted_movies():
    """
    Displays the movies sorted by their rating.
    """
    movies = get_movies()
    sorted_mov = sorted(movies.items(), key=lambda item: item[1][0], reverse=True)
    for movie, details in sorted_mov:
        print(f"{movie}: Rating: {details[0]}, Year: {details[1]}")


# Main Function
def main():
    """
    Main function that initializes the menu loop and managed the user Choice.
    """
    print("********** My Movies Database **********")

    while True:
        print_menu()
        user_main_choice = get_main_choice()
        if user_main_choice == 0:
            print("Bye!")
            break
        handle_user_choice(user_main_choice)


if __name__ == "__main__":
    main()
