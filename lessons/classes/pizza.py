"""Defining a class!"""

from __future__ import annotations 

"""
Think of a class definition as a roadmap for objects 
that belong to the class
You are defining the underlying structure every instance 
of this class will have 
"""

class pizza:
    #attributes 
    #think of these as the variables each instance in my class will have
    #<name> : <type>
    size: str 
    toppings: int 
    gluten_free: bool 

    def __init__(self, input_size: str, input_toppings: int, input_gf: bool): 
        """My constructor"""
        self.size = input_size
        self.toppings = input_toppings
        self.gluten_free = input_gf
        #returns a pizza object 

    def price(self) -> float: 
        """Method to calculate price of pizza."""
        if self.size == "large": 
            price: float = 6.25 
        else: 
            price: float = 5.00 
        price += .75 * self.toppings 
        if self.gluten_free: 
            price += 1.00 
        return price 
    
    def add_toppings(self, num_toppings: int): 
        """Add toppings to pizza."""
        self.toppings += num_toppings 

    def make_new_pizza_add_toppings(self, num_toppings: int) -> pizza:
        """Make a new pizza with existing pizza's properties and additional toppings."""
        new_pizza: pizza = pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    
    def __str__(self) -> str: 
        pizza_info: str = f"Pizza order: size {self.size}, toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info


my_pizza: pizza = pizza("medium", 3, False)
print(str(my_pizza)) 
sals_pizza: pizza = pizza("large", 1, True)
print(sals_pizza) 