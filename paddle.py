from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        p_y = self.ycor() + 50
        self.goto(self.xcor(), p_y)
    def go_down(self):
        p_y = self.ycor() - 50
        self.goto(self.xcor(), p_y)
