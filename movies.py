import random


def main():
    # Dictionary to store the movies and the rating
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    # Your code here
    print("********** My Movies Database **********")

    while True:
        print_menu()
        user_main_choice = get_main_choice()
        if user_main_choice == 0:
            print("Bye!")
            break
        handle_user_choice(user_main_choice, movies)


# Prints the main-menu
def print_menu():
    print("")
    print("Menu:")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")
    print("")


# Gets the user choice for main-menu
def get_main_choice():
    user_main_choice = int(input("Enter choice (1-8): "))
    return user_main_choice


# Handles user choice
def handle_user_choice(choice, movie_dictionary):
    if choice == 1:
        list_movies(movie_dictionary)
    elif choice == 2:
        add_movie(movie_dictionary)
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

    # Choice 1: prints out all moviesy


def list_movies(movie_dictionary):
    total_movies = len(movie_dictionary)
    print("")
    print(f"{total_movies} movies in total")
    print("")
    for key, value in movie_dictionary.items():
        print(f"{key}: {value}")


# Choice 2: Adds a movie
def add_movie(movie_dictionary):
    movie_name = input("Please enter a movie name: ")
    movie_rating = float(input("Please enter the movie's rating: "))
    movie_dictionary[movie_name] = movie_rating
    print(f"The movie '{movie_name}' was added.")


# Choice 3: Deletes a movie
def delete_movie(movie_dictionary):
    movie_name = input("Please enter the name of the movie you want to delete: ")
    movie_value = movie_dictionary.pop(movie_name, None)
    print(f"The movie '{movie_name}' was deleted.")
    if movie_value is None:
        print(f"ERROR! The movie '{movie_name}' does not exists!")


# Choice 4: Updates a movie
def update_movie(movie_dictionary):
    movie_name = input("Which movie do you want to update? Please enter the name: ")
    if movie_name in movie_dictionary:
        new_rating = float(input("Please enter the new rating: "))
        movie_dictionary.update({movie_name: new_rating})
        print(f"The movie '{movie_name}' was updated.")
    else:
        print(f"ERROR! The movie '{movie_name}' does not exists!")


# Choice 5: Shows stats: average rating, median rating, best movie, worst movie
def show_stats(movie_dictionary):
    print("")
    """Average rating"""
    average_rating = sum(movie_dictionary.values()) / len(movie_dictionary)
    print(f"The average rating is: {average_rating}")

    """Median rating"""
    ratings = sorted(movie_dictionary.values())
    n = len(ratings)
    if n % 2 == 0:
        median = (ratings[n // 2 - 1] + ratings[n // 2]) / 2
    else:
        median = ratings[n // 2]
    print(f"The median rating is: {median}")

    """Best movie"""
    max_rating = max(movie_dictionary.values())
    top_movies = [movie for movie, rating in movie_dictionary.items() if rating == max_rating]
    print(f"The top movie(s) are {', '.join(top_movies)} with a rating of {max_rating}.")

    """Worst movie"""
    min_rating = min(movie_dictionary.values())
    worst_movies = [movie for movie, rating in movie_dictionary.items() if rating == min_rating]
    print(f"The worst movie(s) are {', '.join(worst_movies)} with a rating of {min_rating}.")


# Choice 6: Gives back a random movie
def random_choice(movie_dictionary):
    keys_list = list(movie_dictionary.keys())
    r_choice_name = random.choice(keys_list)
    r_choice_rating = movie_dictionary.get(r_choice_name)
    print(f"Your random choice is: '{r_choice_name}'. It's rated with {r_choice_rating}.")


# Choice 7: Search movie
def search_movie(movie_dictionary, search_term):
    search_term_lower = search_term.lower()
    search_result = [movie for movie in movie_dictionary if search_term_lower in movie.lower()]
    if search_result:
        for movie in search_result:
            print(f"{movie},  {movie_dictionary[movie]}")
    else:
        print("Movie not found")


# Choice 8: Shows movies sorted by ranking
def sorted_movies(movie_dictionary):
    sorted_mov = sorted(movie_dictionary.items(), key=lambda item: item[1], reverse=True)
    for movie, rating in sorted_mov:
        print(f"{movie}: {rating}")


if __name__ == "__main__":
    main()
