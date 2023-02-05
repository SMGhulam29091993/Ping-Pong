from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

paddle_right = Paddle((380, 0))
paddle_left = Paddle((-380, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("PONG GAME")
screen.listen()
screen.tracer(0)

screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")
screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting upward wall collision to bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball misses the paddle it reset position & score added
    if ball.xcor() > 380:
        #game_on = False
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Detects paddle and ball bounces back
    if (ball.distance(paddle_right) < 60 and ball.xcor() > 350) or (ball.distance(paddle_left) < 60 and ball.xcor() < -350):
        ball.bounce_x()




screen.exitonclick()
