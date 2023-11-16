"""Practice importing from other modules"""

from lessons import my_functions 

print(my_functions.addition(2,5))

print(my_functions.my_variable)

if __name__ == "__main__": 
    print("Howdy!")


def main() -> None:
     """Main Function"""
     y: int = g(1)
     f(y)
     print(g(f(3)))

def f(x: int) -> int:
     """Function 0"""
     if x % 2 == 0:
         print(f"{x} is even")
     else:
         x += 1
     return x

def g(x: int) -> int:
     """Function 1"""
     while x % 2 == 1:
         x += 1
     return x

main()