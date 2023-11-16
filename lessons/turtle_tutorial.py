from turtle import Turtle, colormode, done 

colormode(255)

leo: Turtle = Turtle()
bob: Turtle = Turtle()

bob.pencolor(5, 5, 0)
bob.speed(100)

bob.penup()
bob.goto(45, 60)
bob.pendown()

leo.fillcolor("pink")
leo.speed(50)

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.begin_fill()
    # code for shape to be filled 
i: int = 0
side_length: int = 300 
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1 
leo.end_fill()

bob.begin_fill()
i: int = 0
side_length: int = 300 
while (i < 3):
    bob.forward(side_length * 0.95)
    bob.left(123)
    i = i + 1
bob.end_fill()

done()

