import time
from turtle import Turtle
ALIGMENT = "center"
FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align=ALIGMENT, font=FONT)
