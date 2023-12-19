import turtle

# Constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SIZE = 3
SEGMENT_SIZE = 20

class Snake(object):
    
    # Constructor
    def __init__(self):
        self.segments = []
        for i in range(SIZE):
            snake_part = turtle.Turtle()
            snake_part.penup()
            snake_part.shape("square")
            snake_part.color("white")
            snake_part.setpos(x=-SEGMENT_SIZE*i, y=0)
            self.segments.append(snake_part)
        self.head = self.segments[0]

    # Move the snake
    def move(self):
        for i in range(SIZE - 1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(SEGMENT_SIZE)
    
    # Turn the snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    # Turn the snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    # Turn the snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Turn the snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
