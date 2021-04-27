from turtle import Turtle


class Ball(Turtle):
    def __init__(self,):
        super().__init__()
        self.shape("circle")
        #self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.penup()
        self.x = 1
        self.y = 1

    def jump(self):
        b_x = self.xcor() + self.x
        b_y = self.ycor() + self.y
        self.goto(b_x, b_y)

    def ricochet(self):
        self.y = -self.y

    def hit(self):
        self.x = -self.x

