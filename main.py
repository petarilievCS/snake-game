import turtle
import time

from snake import Snake

# Screen setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(n=0)

# Snake 
snake = Snake()

# Event listeners
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Game loop
while True:
    screen.update() 
    time.sleep(0.1)
    snake.move()

screen.exitonclick()