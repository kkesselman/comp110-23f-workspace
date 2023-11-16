"""Defining a point with x and y coordinates."""

from __future__ import annotations

__author__: 730395385 


class Point: 
    """Creating a point."""
    x: float
    y: float 

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0): 
        """Initializes the values of x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int): 
        """Scales x and y by a certain factor."""
        self.x = self.x * factor 
        self.y = self.y * factor 

    def scale(self, factor: int) -> Point: 
        """Creates new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point 
    
    def __str__(self) -> str: 
        """Prints out x: <x value>, y: <y value>."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point: 
        """Returns new point multiplied by a factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point: 
        """Adds factor to the x and y attributes."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point