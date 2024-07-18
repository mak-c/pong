from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("PONG 🤫🧏")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

game_is_on = True

while game_is_on:
    if scoreboard.r_score >= 5 or scoreboard.l_score >= 5:
        game_is_on = False
        scoreboard.game_over()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
# detect ball bounce off the roof/floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# detect collision with right paddle
    if ((ball.ycor() <= r_paddle.ycor() + 50) and (ball.ycor() >= r_paddle.ycor() - 50) and
            (ball.xcor() == r_paddle.xcor() - 20)):
        ball.bounce_x()

# detect collision with left paddle
    if ((ball.ycor() <= l_paddle.ycor() + 50) and (ball.ycor() >= l_paddle.ycor() - 50) and
            (ball.xcor() == l_paddle.xcor() + 20)):
        ball.bounce_x()

# detect if ball has missed (goes OOB), reset ball and add score to other payers score
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
