from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Establish the screen configurations
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Pong Game")
screen.tracer(0)

# Instances of the created classes
paddle_r = Paddle((450, 0))
paddle_l = Paddle((-450, 0))
ball = Ball()
score = Score()

screen.update()

screen.listen()
screen.onkey(paddle_r.up_paddle, "Up")
screen.onkey(paddle_r.down_paddle, "Down")
screen.onkey(paddle_l.up_paddle, "w")
screen.onkey(paddle_l.down_paddle, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.update_score()

    if ball.ycor() > 370 or ball.ycor() < -370:
        ball.bounce_y()

    if (ball.xcor() > 430 and ball.distance(paddle_r) < 80) or (ball.xcor() < -430 and ball.distance(paddle_l) < 80):
        ball.bounce_x()

    if ball.xcor() > 440:
        score.point_left()
        paddle_r.restart((450, 0))
        paddle_l.restart((-450, 0))
        ball.restart()
        ball.bounce_y()
        ball.bounce_x()

    if ball.xcor() < -440:
        score.point_right()
        paddle_r.restart((450, 0))
        paddle_l.restart((-450, 0))
        ball.restart()

screen.exitonclick()
