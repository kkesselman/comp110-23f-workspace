"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730395385"

five_character_word: str = input("Enter 5-character word: ")
if len(five_character_word) != 5: 
    print("Error: Word must contain 5 characters")
    exit()

single_letter: str = input("Enter a single character: ")
if len(single_letter) != 1: 
    print("Error: Character must be a single character.") 
    exit()
else:
    print("Searching for " + single_letter + " in " + five_character_word)
    

matches: int = 0 

if single_letter == str(five_character_word[0]):
    print(single_letter + " found at index 0") 
    matches = matches + 1 
if single_letter == str(five_character_word[1]):
    print(single_letter + " found at index 1") 
    matches = matches + 1 
if single_letter == str(five_character_word[2]):
    print(single_letter + " found at index 2") 
    matches = matches + 1 
if single_letter == str(five_character_word[3]):
    print(single_letter + " found at index 3") 
    matches = matches + 1 
if single_letter == str(five_character_word[4]):
    print(single_letter + " found at index 4") 
    matches = matches + 1 

if matches == 0: 
    print("No instances of " + single_letter + " found in " + five_character_word)
if matches == 1:
    print(str(matches) + " instance of " + single_letter + " found in " + five_character_word)
if matches > 1:  
    print(str(matches) + " instances of " + single_letter + " found in " + five_character_word)