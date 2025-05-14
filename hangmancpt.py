# Hangman Student Developed Code:
# Used Chatgpt to help with the display_hangman(attempts) section to get hangman to show up and helped with the structure and layout of all the code.

import random
import os

# List Part 1: Words for the hangman game (csp vocabulary)
word_list = [
    "python", "hangman", "computer", "programming", "algorithm",
    "dictionary", "function", "variable", "developer", "iteration"
]

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(attempts):
    """Returns a hangman figure based on remaining attempts."""
    stages = [
        "  --------\n  |      |\n  |\n  |\n  |\n  |\n  -",
        "  --------\n  |      |\n  |      O\n  |\n  |\n  |\n  -",
        "  --------\n  |      |\n  |      O\n  |      |\n  |      |\n  |\n  -",
        "  --------\n  |      |\n  |      O\n  |     \\|\n  |      |\n  |\n  -",
        "  --------\n  |      |\n  |      O\n  |     \\|/\n  |      |\n  |\n  -",
        "  --------\n  |      |\n  |      O\n  |     \\|/\n  |      |\n  |     /\n  -",
        "  --------\n  |      |\n  |      O\n  |     \\|/\n  |      |\n  |     / \\\n  -"
    ]
    return stages[6 - attempts]

# Student Developed Procedure Part 1: Sequencing,
def handle_guess(secret_word, guess, display, guessed_letters):
    
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'")
        return None

    guessed_letters.append(guess)
    correct = False

    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            display[i] = guess
            correct = True

    return correct

# Main gameplay function
def hangman_game():
    print("===== Welcome to Hangman! =====")

    # List Part 2: List used to manage complexity
    secret_word = random.choice(word_list).upper()
    display = ["_"] * len(secret_word)
    guessed_letters = []
    attempts = 6

    while attempts > 0 and "_" in display:
        print("\n" + display_hangman(attempts))
        print("Word: " + " ".join(display))
        print("Guessed Letters: " + ", ".join(guessed_letters))
        print(f"Attempts Left: {attempts}")

        guess = input("Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        # Student Developed Procedure Part 2: Call to the Procedure
        result = handle_guess(secret_word, guess, display, guessed_letters)

        if result is None:
            continue
        elif result:
            print(f"Nice! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

    print("\n" + display_hangman(attempts))
    print("Word: " + " ".join(display))

    if "_" not in display:
        print(f"🎉 You guessed it! The word was {secret_word}.")
    else:
        print(f"💀 Game Over. The word was {secret_word}.")

def main():
    while True:
        hangman_game()
        again = input("Play again? (Y/N): ").upper()
        if again != "Y":
            print("Goodbye!")
            break
        clear_screen()

if __name__ == "__main__":
    main()
