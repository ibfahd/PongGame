from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.rScore = 0
        self.lScore = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(200, 200)
        self.write(self.rScore, align="center", font=("Digitechno", 36, "bold"))
        self.goto(-200, 200)
        self.write(self.lScore, align="center", font=("Digitechno", 36, "bold"))

    def rScoreUp(self):
        self.rScore += 1
        self.update()
    
    def lScoreUp(self):
        self.lScore += 1
        self.update()

