import os
import random
from game_data import data
from art import logo


def format_data(game_data: dict) -> str:
    """Get and formats the data."""
    name = game_data["name"]
    description = game_data["description"]
    country = game_data["country"]

    return f"{name}, a {description} from {country}"


def compare(user_guess: str, followers_a: int, followers_b: int) -> bool:
    """Checks the answer and return True or False.
    :param: user_guess -> user input if it's 'a' or 'b'
            followers_a/b -> from game_data[followers_count]
    """
    if followers_a > followers_b:
        return user_guess == "a"
    else:
        return user_guess == "b"


def clrscr():
    """Clears the output console."""
    os.system("cls" if os.name == "nt" else "clear")


is_game_over = False
score = 0

item_a = random.choice(data)
item_b = random.choice(data)


while not is_game_over:

    #prevents having the same data
    if item_a == item_b:
        item_b = random.choice(data)


    print(logo)
    print(format_data(item_a))
    print("VS.")
    print(format_data(item_b))

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    clrscr()
    item_a_followers = item_a["follower_count"]
    item_b_followers = item_b["follower_count"]

    is_correct = compare(guess, item_a_followers, item_b_followers)

    if is_correct:
        score += 1
        print(f"You're correct! Current score: {score}")
        #unpacking and re-assigning values
        #prev becomes item_a, item_a becomes item_b and item_b with new random game data
        previous, item_a, item_b = item_a, item_b, random.choice(data)
    else:
        print(f"Oops. Wrong! Final score: {score}")
        is_game_over = True

