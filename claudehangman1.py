import random
import os

def clear_screen():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def display_hangman(attempts):
    """
    Displays the hangman figure based on the number of incorrect attempts.
    
    Parameters:
        attempts (int): The number of incorrect guesses made by the player
        
    Returns:
        str: The hangman ASCII art corresponding to the attempt count
    """
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |     
           -
        """
    ]
    return stages[attempts]

def initialize_word_bank():
    """
    Creates and returns a list of words for the hangman game.
    
    Returns:
        list: A list containing 20 words for the game
    """
    # Collection/List being used to manage complexity - REQUIREMENT #3
    word_bank = [
        "python", "hangman", "computer", "programming", "algorithm",
        "dictionary", "function", "variable", "developer", "iteration",
        "keyboard", "monitor", "challenge", "solution", "database",
        "network", "interface", "application", "security", "framework"
    ]
    return word_bank

def select_random_word(words):
    """
    Selects a random word from the provided list.
    
    Parameters:
        words (list): List of words to choose from
        
    Returns:
        str: A randomly selected word from the list
    """
    # Using data from the list - REQUIREMENT #4
    return random.choice(words).upper()

def play_hangman():
    """
    Main procedure to run the hangman game.
    """
    print("\n===== WELCOME TO HANGMAN =====")
    print("Try to guess the hidden word one letter at a time!")
    
    # Initialize the game
    word_bank = initialize_word_bank()
    word = select_random_word(word_bank)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    
    print(display_hangman(attempts))
    print(f"Word: {' '.join(word_completion)}")
    print("\n")
    
    # Main game loop
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        # Process single letter guess
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                
                # Update the displayed word with correctly guessed letters
                word_completion = update_word_display(guess, word, word_completion)
                if "_" not in word_completion:
                    guessed = True
        
        # Process word guess
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        
        # Handle invalid input
        else:
            print("Not a valid guess. Please enter a single letter or the full word.")
        
        # Display game state after each guess
        clear_screen()
        print(display_hangman(attempts))
        print(f"Word: {' '.join(word_completion)}")
        print(f"Letters guessed: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
    # Game result
    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word}")

def main():
    """
    Main function that controls the game flow.
    """
    play_game = True
    
    while play_game:
        play_hangman()
        
        while True:
            play_again = input("Would you like to play again? (Y/N): ").upper()
            if play_again == 'Y':
                break
            elif play_again == 'N':
                play_game = False
                print("Thanks for playing!")
                break
            else:
                print("Please enter Y or N.")

if __name__ == "__main__":
    main()