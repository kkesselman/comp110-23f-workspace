"""File to define Bear class."""


class Bear:
    """Creating bear object for river."""
    age: int 
    hunger_score: int 

    def __init__(self):
        """Create bear."""
        self.age = 0
        self.hunger_score = 0 
        return None
    
    def one_day(self):
        """Add one to bear age."""
        self.age += 1 
        self.hunger_score -= 1
        return None 
    
    def eat(self, num_fish: int): 
        """Describes how many fish a bear eats and how hunger it still is."""
        self.hunger_score += num_fish
        return None 