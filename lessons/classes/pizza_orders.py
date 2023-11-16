"""Instantiating a class."""

"""
This is where we instantiate the class we defined in classes.py
Creating objects that belong to that class. 
"""

from lessons.classes.pizza import pizza 

my_pizza: pizza = pizza("large", 10, True) #constructor 

#setting attributes 
my_pizza.size = "medium" #updates size of my_pizza 
#my_pizza.toppings = 10 
#my_pizza.gluten_free = True 

print(my_pizza.toppings)
print(my_pizza.size)

sals_pizza: pizza = pizza("medium", 5, False)

def price(inp_pizza: pizza) -> float: 
    """Function to calculate price of pizza."""
    if inp_pizza.size == "large": 
        price: float = 6.25 
    else: 
        price: float = 5.00 
    price += .75 * inp_pizza.toppings 
    if inp_pizza.gluten_free: 
        price += 1.00 
    return price 

#calling price function
print(price(sals_pizza))
print(price(my_pizza))

#calling price method
print(sals_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
