# Stephen Randall
# 10/5/17
# Folder: Unit5proj File: unit5project.py
# This program is a simple guessing number game, generates a random number in between 1 and 100, gives hints on whether
# you are too high or too low, counts how many times you've guessed.

import random


def play_the_game():
    """
    This function contains the actual game. Generates number between 1 and 100, Tells user the range of the random
    number. Asks user for guess, resets their number of guess count to 0. Starts a while loop condition is if the player
    guess does not equal the random generated number then start loop. if player guess is greater then the number Tell
    player same goes for if it's too low, each guess is counted. Breaks the loop once you guess correctly.
    This function is called in main()
    """
    gen_number = random.randint(1, 100)
    print("Ok, I'm thinking of a WHOLE number between 1 and 100. Guess what it is!")
    player_guess = int(input("Guess?"))
    num_guesses = 0
    while player_guess != gen_number:
        if player_guess > gen_number:
            print("Your guess was too high!")
        elif player_guess < gen_number:
            print("Dang, your guess was too low!")
        print("Ok, keep guessing!")
        num_guesses += 1
        player_guess = int(input("Guess?"))
    num_guesses += 1
    print("Wow! You're correct! Nice job!", num_guesses)


def main():
    print("Welcome! This is a simple guessing game. Would you like to play? press 'y' for yes and 'n' for no ")
    play_game = input("Play?")
    while play_game in ['y', 'Yes', 'Y', 'YES', 'Sure', 'Why not', 'SURE']:
        play_the_game()
        play_game = input("Play?")
    print("Okay, bye! Thanks for coming!")

main()
