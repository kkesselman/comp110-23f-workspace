"""File to define Fish class."""


class Fish:
    """Creating fish object for river."""
    age: int 

    def __init__(self):
        """Create a fish."""
        self.age = 0 
        return None
    
    def one_day(self):
        """Add one to fish age."""
        self.age += 1 
        return None