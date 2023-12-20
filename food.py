import turtle
import random

MARGIN = 20

class Food(turtle.Turtle):

    # Constructor
    def __init__(self, screen_width, screen_height, snake):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.max_x = screen_width/2 - MARGIN
        self.max_y = screen_height/2 - MARGIN
        self.refresh()
        self.snake = snake

    # Move to a random position
    def refresh(self):
        x = random.randint(-self.max_x, self.max_x)
        y = random.randint(-self.max_y, self.max_y)
        self.goto(x, y)