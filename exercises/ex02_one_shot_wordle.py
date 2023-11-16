"""One Shot Wordle - Guess secret word in one try."""

__author__ = "730395385"

secret_word = "python"

# establish variables for emojis
WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"

emoji = ""

guess_idx = 0 
sec_word_idx = 0 
current_idx: str = ""
current_idx_sec_word: str = ""
playing: bool = True 

# prompt for guess
guess = input("What is your 6-letter guess? ")

# make sure guess is exactly 6 letters
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again! ")

# check for correct letters in correct places (green)
if guess == secret_word: 
    while guess_idx < len(secret_word): 
        current_idx = guess[guess_idx]
        current_idx_sec_word = secret_word[sec_word_idx]
        if current_idx == current_idx_sec_word: 
            emoji += GREEN_BOX
        guess_idx += 1 
        sec_word_idx += 1 
    print(emoji)
    print("Woo! You got it! ")
    playing = False 

while playing: 
    if guess != secret_word: 
        while guess_idx < len(secret_word): 
            current_idx = guess[guess_idx]
            current_idx_sec_word = secret_word[sec_word_idx]
            if current_idx == current_idx_sec_word: 
                emoji += GREEN_BOX
            # checking for incorrect letter (white)
            elif current_idx not in secret_word:
                emoji += WHITE_BOX
            # checking for correct letter somewhere else in word (yellow)
            else: 
                emoji += YELLOW_BOX
            guess_idx += 1 
            sec_word_idx += 1 
    playing = False 
    print(emoji)
    print("Not quite. Play again soon! ") 
