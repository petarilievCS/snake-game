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
            self.grow()
        self.head = self.segments[0]

    # Check collision with tail
    def is_collided(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < SEGMENT_SIZE / 2:
                return True
        return False
    
    # Grow the snake
    def grow(self):
        # Last segment info
        x, y = 0, 0
        if self.segments:
            last_segment = self.segments[-1]
            x = last_segment.xcor()
            y = last_segment.ycor()
            
        # New segment
        snake_part = turtle.Turtle()
        snake_part.penup()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.setpos(x=x-SEGMENT_SIZE, y=y)
        self.segments.append(snake_part)

    # Move the snake
    def move(self):
        size = len(self.segments)
        for i in range(size - 1, 0, -1):
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
