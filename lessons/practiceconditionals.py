"""Practice writing program that prints Right is number is 10 and wrong if it's not"""

my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)

if my_number == 10:
    print("Right")
else: 
    print("Wrong")
