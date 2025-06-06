import random
import ascii_art


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Prints the stage of the meting snowman + (not) guessed letters."""
    if mistakes == 0:
        print(ascii_art.STAGES[1])
    elif mistakes == 1:
        print(ascii_art.STAGES[2])
    elif mistakes == 2:
        print(ascii_art.STAGES[3])
    for letter in secret_word:
        if letter not in guessed_letters:
            print('_', end=' ')
        elif letter in guessed_letters:
            print(letter, end=' ')
    print()


def play_game():
    """Contains greeting and game loop (incl. check if won or not)."""
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print(ascii_art.STAGES[0])

    mistakes = 0
    guessed_letters = []

    while mistakes < 3:
        # Input validation
        while True:
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1:
                print("Please enter only a single letter.")
            elif not guess.isalpha():
                print("Please enter a valid letter (no numbers / symbols).")
            elif guess in guessed_letters:
                print("You already guessed that letter.")
            else:
                break

        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters)

        # Check for win
        if all(letter in guessed_letters for letter in secret_word):
            print(f"You guessed the word: {secret_word}")
            return

    # If loop ends, player has lost
    print(f"Game Over! The word was: {secret_word}")