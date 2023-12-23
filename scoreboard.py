import turtle
import os

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
HIGHSCORE_FILE = "high_score.txt"

class Scoreboard(turtle.Turtle):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, y)
        self.score = 0
        
        if os.path.isfile(HIGHSCORE_FILE):
            # Read previous high score
            with open(HIGHSCORE_FILE) as f:
                self.highscore = int(f.read())
        else:
            self.highscore = 0

    # Increase score    
    def increase_score(self):
        self.score += 1

        if self.score > self.highscore:
             # Save high score
            print("Runs")
            with open(HIGHSCORE_FILE, mode="w") as f:
                f.write(str(self.score))    

        self.highscore = max(self.highscore, self.score)
        self.write_score()

    # Write score
    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    # Write a message
    def write_message(self, message):
        self.write(message, align=ALIGNMENT, font=FONT)

    # Resets score
    def reset(self):
        self.score = 0
        self.write_score()
    