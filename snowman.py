import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Game Loop
    mistakes = 0
    bad_input = True
    while mistakes < 3:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        mistakes += 1


if __name__ == "__main__":
    play_game()