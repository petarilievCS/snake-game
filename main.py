import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Snake Game")

# Snake 
for i in range(3):
    snake_part = turtle.Turtle()
    snake_part.shape("square")
    snake_part.color("white")
    snake_part.setpos(x=-20*i, y=0)

screen.exitonclick()