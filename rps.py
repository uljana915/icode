"""Simple version of rock paper and scissors."""
from random import choice


def normalize_user_name(name: str) -> str:
    """
    Simple function gets player name as input and capitalizes it.

    :param name: name of the player
    :return: A name that is capitalized.
    """
    return name.capitalize()


def reverse_user_name(name: str) -> str:
    """
    Function that takes in name as a parameter and reverses its letters. The name should also be capitalized.

    :param name: name of the player
    :return: A name that is reversed.
    """
    return name[::-1].capitalize()


def check_user_choice(user_choice: str) -> ():
    """
    Function that checks user's choice.

    The choice can be uppercase or lowercase string, but the choice must be
    either rock, paper or scissors. If it is, then return a choice that is lowercase.
    Otherwise return 'Sorry, you entered unknown command.'
    :param choice: user choice
    :return: choice or an error message
    """
    user_choice = user_choice.lower()
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        return "Sorry, you entered unknown command."
    else:
        return user_choice


def determine_winner(name: str, user_choice: str, computer_choice: str, reverse_name: bool = False) -> str:
    """
    Determine the winner returns a string that has information about who won.

    You should use the functions that you wrote before. You should use check_user_choice function
    to validate the user choice and use normalize_user_name for representing a correct name. If the
    function parameter reverse is true, then you should also reverse the player name.
    NB! Use the previous functions that you have written!

    :param name:player name
    :param user_choice:
    :param computer_choice:
    :param reverse_name:
    :return:
    """
    if reverse_name:
        name = reverse_user_name(name)
    name = normalize_user_name(name)
    user_choice = user_choice.lower()
    computer_choice = computer_choice.lower()
    if computer_choice not in {"paper", "scissors", "rock"}:
        return "There is a problem determining the winner."
    if user_choice == computer_choice:
        return f"{name} had {user_choice} and computer had {computer_choice}, hence it is a draw."
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return f"{name} had {user_choice} and computer had {computer_choice}, hence {name} wins."
        else:
            return f"{name} had {user_choice} and computer had {computer_choice}, hence computer wins."
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return f"{name} had {user_choice} and computer had {computer_choice}, hence computer wins."
        else:
            return f"{name} had {user_choice} and computer had {computer_choice}, hence {name} wins."
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return f"{name} had {user_choice} and computer had {computer_choice}, hence {name} wins."
        else:
            return f"{name} had {user_choice} and computer had {computer_choice}, hence computer wins."
    else:
        return "There is a problem determining the winner."


def play_game() -> None:
    """
    Enable you to play the game you just created.
    :return:
    """
    user_name = input("What is your name? ")
    play_more = True
    while play_more:
        computer_choice = choice(['rock', 'paper', 'scissors'])
        user_choice = check_user_choice(input("What is your choice? "))
        print(determine_winner(user_name, user_choice, computer_choice))
        play_more = True if input("Do you want to play more ? [Y/N] ").lower() == 'y' else False

# play_game() # Kommenteeri see rida välja kui kõik funktsioonid on valmis