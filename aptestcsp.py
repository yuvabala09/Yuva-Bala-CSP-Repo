import random

# List: Where the words are stored (requirement for list storage)
word_list = ["python", "hangman", "challenge", "student", "programming", "function"]

# Procedure: Student-developed procedure that includes sequencing, selection, iteration, and uses a parameter
def process_guess(word, display, guess):
    """
    This function updates the display list with the guessed letter if it's in the word.
    Parameters:
    - word: the secret word
    - display: the current state of guessed letters and blanks
    - guess: the letter guessed by the user
    """
    correct = False
    for index in range(len(word)):
        if word[index] == guess:
            display[index] = guess
            correct = True
    return correct  # Return True if the guess was correct, otherwise False

# Start of the program
def hangman_game():
    print("Welcome to Hangman! Let's start the game.")

    # 2. Randomly choosing a word from the list (using list for managing complexity)
    secret_word = random.choice(word_list)
    display_word = ["_"] * len(secret_word)  # blank spots

    lives = 7
    guessed_letters = []  # list to store guessed letters

    while lives > 0 and "_" in display_word:
        print("\nWord: " + " ".join(display_word))
        print(f"Lives remaining: {lives}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        # 3. Calling the student-developed procedure
        if process_guess(secret_word, display_word, guess):
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            lives -= 1

    # Final outcome
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nGame Over. The word was:", secret_word)

# 4. Calling the main function to start the game
hangman_game()