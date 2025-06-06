import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    if mistakes == 0:
        print(STAGES[1])
    elif mistakes == 1:
        print(STAGES[2])
    elif mistakes == 2:
        print(STAGES[3])
    for letter in secret_word:
        if letter not in guessed_letters:
            print('_', end=' ')
        elif letter in guessed_letters:
            print(letter, end=' ')
    print()


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print(STAGES[0])
    for letter in secret_word:
        print(letter, end='')
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Game Loop
    mistakes = 0
    guessed_letters = []
    bad_input = True
    while mistakes < 3:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess in secret_word:
            guessed_letters.append(guess)
        display_game_state(mistakes, secret_word, guessed_letters)
        if guess not in secret_word:
            mistakes += 1

    #End of game
    if len(secret_word) == len(guessed_letters):
        print(f"Word guessed: {secret_word}")
    else:
        print(f"Game Over! The word was: {secret_word}")



if __name__ == "__main__":
    play_game()