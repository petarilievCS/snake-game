import turtle
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
THRESHOLD = 15

# Screen setup
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(n=0)

# Snake 
snake = Snake()
food = Food(screen_width=WIDTH, screen_height=HEIGHT, snake=snake)
scoreboard = Scoreboard(x=0, y=HEIGHT/2 - 50)

# Event listeners
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

def reset():
    scoreboard.reset()
    snake.reset() 

# Game loop
while True:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    scoreboard.write_score()

    # Check for collision with food
    if snake.head.distance(food) < THRESHOLD:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()
    
    # Check for collision with wall
    if snake.head.xcor() > WIDTH/2 or snake.head.xcor() < -WIDTH/2 or snake.head.ycor() > HEIGHT/2 or snake.head.ycor() < -HEIGHT/2:
        reset()

    # Check snake collision
    if snake.is_collided():
        reset()

screen.exitonclick()