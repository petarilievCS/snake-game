import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(n=0)

# Snake 
snake = []
for i in range(3):
    snake_part = turtle.Turtle()
    snake_part.penup()
    snake_part.shape("square")
    snake_part.color("white")
    snake_part.setpos(x=-20*i, y=0)
    snake.append(snake_part)

# Game loop
while True:
    screen.update() 
    time.sleep(0.1)
    num_segments = len(snake)
    for i in range(num_segments - 1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)
    snake[0].forward(20)

screen.exitonclick()