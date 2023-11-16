from turtle import Turtle, colormode, done
import random 

colormode(255)

def draw_mountain(pen, width, height, color, outline_color):
    """Set up the function to draw the mountains."""
    pen.fillcolor(color)
    pen.pencolor(outline_color)
    pen.begin_fill()
    for _ in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_cloud(pen, x, y, size):
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

def main():
    """Run the main program to draw the scene."""
    screen = Turtle().screen
    screen.bgcolor((52, 227, 255))

    mountain_colors = [(107, 95, 82), (64, 36, 8), (64, 64, 8)]
    outline_color = (80, 49, 18)

    # Draw three mountains in set positions
    positions = [(-150, -150), (0, -150), (150, -150)]
    for pos in positions:
        pen = Turtle()
        pen.speed(1)
        pen.penup()
        pen.goto(pos)
        pen.pendown()
        draw_mountain(pen, 200, 150, random.choice(mountain_colors), outline_color)

    # Draw clouds in set positions
    cloud_positions = [(-150, 100), (0, 120), (150, 80)]
    pen = Turtle()
    pen.speed(1)
    for pos in cloud_positions:
        draw_cloud(pen, pos[0], pos[1], 30)

    # Draw the sun in a set position
    pen = Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(200, 200)
    pen.pendown()
    pen.shape("circle")
    pen.shapesize(3)
    pen.color((255, 255, 0)) 

    done()

if __name__ == "__main__":
    main()