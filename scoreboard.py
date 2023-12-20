import turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(turtle.Turtle):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, y)
        self.score = 0
    
    # Increase score    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Write score
    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Write a message
    def write_message(self, message):
        self.write(message, align=ALIGNMENT, font=FONT)
    
