import random

def get_random_word(word_list):
    return random.choice(word_list)

def display_game_state(word, guessed_letters, incorrect_guesses, hangman_stages):
    display = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"\nCurrent word: {display}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters | incorrect_guesses))}")
    print(f"Incorrect guesses left: {len(hangman_stages) - len(incorrect_guesses)}")
    print(hangman_stages[len(incorrect_guesses)])
    
def get_player_guess():
    guess = input("Guess a letter: ").lower()
    while len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        guess = input("Guess a letter: ").lower()
    return guess

def choose_difficulty():
    difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid choice. Please choose easy, medium, or hard.")
        difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'medium':
        return 7
    else:
        return 5

def play_hangman():
    word_list = ["python", "hangman", "programming", "openai", "developer"]
    hangman_stages = [
        """
         -----
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]

    word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = set()
    max_incorrect_guesses = choose_difficulty()
    
    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    
    while True:
        display_game_state(word, guessed_letters, incorrect_guesses, hangman_stages)
        guess = get_player_guess()
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter. Try again.")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            if all(letter in guessed_letters for letter in word):
                display_game_state(word, guessed_letters, incorrect_guesses, hangman_stages)
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect guess.")
            if len(incorrect_guesses) >= max_incorrect_guesses:
                display_game_state(word, guessed_letters, incorrect_guesses, hangman_stages)
                print(f"Sorry, you've run out of guesses. The word was: {word}")
                break

if __name__ == "__main__":
    play_hangman()
