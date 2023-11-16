"""Draws a mountain scene of my hometown in Colorado.

I have broken up the main function into multiple functions, used the circle and pos turtle methods,
and used the random function to produce random mountain colors.
"""


__author__ = "730395385"
from turtle import Turtle, colormode, done
import random 

colormode(255)


def draw_mountain(pen: Turtle, width: int, height: int, color: tuple[int, int, int], outline_color: tuple[int, int, int]) -> None:
    """Set up the function to draw the mountains."""
    pen.fillcolor(color)
    pen.pencolor(outline_color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()


def draw_cloud(pen: Turtle, x: int, y: int, size: int) -> None:
    """Set up the function to draw the clouds."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    for _ in range(4):
        pen.circle(size)
        pen.right(90)
    pen.end_fill()


def main() -> None:
    """Run the main program to draw the scene."""
    screen = Turtle().screen
    screen.bgcolor((52, 227, 255))

    mountain_colors = [(107, 95, 82), (64, 36, 8), (64, 64, 8)]
    outline_color = (80, 49, 18)

    # Draw three mountains in set positions
    positions = [(-150, -150), (0, -150), (150, -150)]
    for pos in positions:
        pen = Turtle()
        pen.speed(50)
        pen.penup()
        pen.goto(pos)
        pen.pendown()
        draw_mountain(pen, 200, 150, random.choice(mountain_colors), outline_color)

    # Draw clouds in set positions
    cloud_positions = [(-150, 100), (0, 120), (150, 80)]
    pen = Turtle()
    pen.speed(50)
    for pos in cloud_positions:
        draw_cloud(pen, pos[0], pos[1], 30)

    # Draw the sun in a set position
    pen = Turtle()
    pen.speed(50)
    pen.penup()
    pen.goto(200, 200)
    pen.pendown()
    pen.shape("circle")
    pen.shapesize(3)
    pen.color((255, 255, 0)) 

    done()


if __name__ == "__main__":
    main()