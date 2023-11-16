"""Wordle with six tries to guess the secret word."""


__author__ = "730395385"


def contains_char(secret_word: str, guess_chr: str) -> bool: 
    """Checking if a character is in the secret word."""
    assert len(guess_chr) == 1
    num_i: int = 0
    while num_i < len(secret_word): 
        if guess_chr == secret_word[num_i]: 
            return True 
        num_i += 1 
    return False 


# Establish variables for emojis
WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def emojified(guess_word: str, secret_word: str) -> str: 
    """Assign emojis to characters."""
    num_i: int = 0 
    emoji: str = ""
    assert len(guess_word) == len(secret_word)
    while num_i < len(secret_word):  
        if secret_word[num_i] == guess_word[num_i]: 
            emoji += GREEN_BOX
        elif contains_char(secret_word, guess_word[num_i]): 
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX
        num_i += 1 
    return emoji 


def input_guess(length: int) -> str: 
    """Ensure that guess is the correct length."""
    guess_word: str = input(f"Enter a {length} character word: ")
    if len(guess_word) != length: 
        guess_word = input(f"That wasn't {length} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    num_of_tries: int = 1
    continue_playing: bool = True

    while num_of_tries <= 6 and continue_playing:
        print(f"=== Turn {num_of_tries}/6 ===")
        guess_word: str = input_guess(len(secret_word))
        feedback = emojified(guess_word, secret_word)
        print(feedback) 

        if guess_word == secret_word: 
            print(f"You won in {num_of_tries}/6 turns!")
            continue_playing = False 
        else: 
            num_of_tries += 1 
    if num_of_tries == 7: 
        continue_playing = False
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()