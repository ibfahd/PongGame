from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

game_is_on = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


rPaddle=Paddle((350,0))
lPaddle=Paddle((-350,0))
pongBall = Ball()
scoreboard = Score()

def stop():
    global game_is_on
    game_is_on = False

screen.listen()
screen.onkey(rPaddle.go_up,"Up")
screen.onkey(rPaddle.go_down,"Down")
screen.onkey(lPaddle.go_up,"q")
screen.onkey(lPaddle.go_down,"w")
screen.onkey(stop,"x")

while game_is_on:
    time.sleep(0.01)
    screen.update()

    if (pongBall.ycor() == 290) or (pongBall.ycor() == -280):
        pongBall.ricochet()
    pongBall.jump()

    if (pongBall.distance(rPaddle) <= 60) and (pongBall.xcor() == 330) or (pongBall.distance(lPaddle) <= 60) and (pongBall.xcor() == -330):
        pongBall.hit() 

    if (pongBall.xcor() == 390):
        scoreboard.lScoreUp()
        pongBall.reset()
        pongBall.hit()
    
    if (pongBall.xcor() == -390):
        scoreboard.rScoreUp()
        pongBall.reset()
        pongBall.hit()
       


screen.exitonclick()