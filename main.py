from storage_json import StorageJson
from movie_app import MovieApp



def print_menu():
    """
    Prints the main menu options for the user.
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


def handle_user_choice(choice, movie_app_instance):
    """
    Handles the user's choice from the main menu and calls the appropriate function.
    :param choice (int): The user's menu choice.
    :param movie_app_instance (MovieApp): The movie app instance handling the operations.
    """
    if choice == 1:
        movie_app_instance._command_list_movies()
    elif choice == 2:
        title = input("Please enter a movie name: ")
        rating = float(input("Please enter the movie's rating: "))
        year = int(input("Please enter the year of release: "))
        movie_app_instance._command_add_movie(title, year, rating)
    elif choice == 3:
        title = input("Please enter the name of the movie you want to delete: ")
        movie_app_instance._command_delete_movie(title)
    elif choice == 4:
        title = input("Which movie do you want to update? Please enter the name: ")
        rating = float(input("Please enter the new rating: "))
        movie_app_instance._command_update_movie(title, rating)
    elif choice == 5:
        movie_app_instance._command_movie_stats()
    elif choice == 6:
        movie_app_instance._command_random_choice()
    elif choice == 7:
        search_term = input("Enter a part of a movie name: ")
        movie_app_instance._command_search_movie(search_term)
    elif choice == 8:
        movie_app_instance._command_sorted_movies()
    else:
        print("Wrong number, please choose again!")


# Main Function
def main():
    """
    Main function that initializes the menu loop and managed the user Choice.
    """
    print("********** My Movies Database **********")
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)

    while True:
        print_menu()
        user_main_choice = get_main_choice()
        if user_main_choice == 0:
            print("Bye!")
            break
        handle_user_choice(user_main_choice, movie_app)


if __name__ == "__main__":
    main()