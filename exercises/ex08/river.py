"""File to define River class."""

__author__ = "730395385"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Creating River with bears and fish."""
    day: int 
    bears: list[Bear] = []
    fish: list[Fish] = []

    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish and bears that are too old."""
        # Remove fish with age > 3 
        new_fish_list = []
        for fish in self.fish: 
            if fish.age <= 3: 
                new_fish_list.append(fish)
        self.fish = new_fish_list

        # Remove bears with age > 5 
        new_bear_list = []
        for bear in self.bears: 
            if bear.age <= 5: 
                new_bear_list.append(bear)
        self.bears = new_bear_list
        return None
    
    def remove_fish(self, amount: int): 
        """Remove amount of fish from River."""
        idx: int = 0 
        while idx < amount: 
            self.fish.pop(idx)
            idx += 1 

    def bears_eating(self):
        """Adjust fish and hunger levels when bears eat."""
        for bear in self.bears: 
            if len(self.fish) > 4: 
                self.remove_fish(3)
                bear.eat(3) 
        return None
    
    def check_hunger(self):
        """Check how hungry bears are."""
        new_bear_list = []
        for bear in self.bears: 
            if bear.hunger_score >= 0: 
                new_bear_list.append(bear) 
        self.bears = new_bear_list
        return None
        
    def repopulate_fish(self):
        """Repopulate fish for every pair produce 4 new fish."""
        new_fish: int = len(self.fish) // 2
        for _ in range(new_fish * 4): 
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulate bears for every pair produce 1 new bear."""
        new_bears: int = len(self.bears) // 2 
        for _ in range(new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """View river simulation."""
        print(f"~~~ Day {str(self.day)}: ~~~ \n Fish population: {len(self.fish)} \n Bear population: {len(self.bears)}") 
        return None
        
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        for bear in self.bears:
            bear.hunger_score -= 1 
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self): 
        """Call one_river_day seven times."""
        for x in range(7): 
            self.one_river_day()
        return None 


my_river = River(num_fish=10, num_bears=2)
my_river.one_river_week() 