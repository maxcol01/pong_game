from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score_board import Score

# create the screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# create the paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
# create the ball
pong_ball = Ball()
# create the score board
score1 = Score(0, (-100, 200))
score2 = Score(0, (100, 200))

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "a")
screen.onkey(l_paddle.move_down, "q")
is_on = True
direction = [10, 15]
t = 0.1
while is_on:
    time.sleep(t)
    screen.update()
    # create the automatic motion
    pong_ball.move_ball(direction)
    # detect collision with paddle: condition --> same xcor() (with tolerance) and same ycor() +/- size of paddle
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(
            l_paddle) < 50 and pong_ball.xcor() < -320:
        direction[0] *= -1
        t -= 0.01

    # check if the ball goes beyond the game limits:
    if pong_ball.off_limit(direction):
        score1.clear()
        score2.clear()
        score1 = Score(pong_ball.player1_score, (-100, 200))
        score2 = Score(pong_ball.player2_score, (100, 200))
        pong_ball.goto(0, 0)
        t = 0.1

screen.exitonclick()
