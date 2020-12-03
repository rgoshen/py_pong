from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# variables
game_is_on = True
SCORE_LIMIT = 21

# objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

# event listeners
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# main
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # game over
    if scoreboard.l_score == SCORE_LIMIT or scoreboard.r_score == SCORE_LIMIT:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
