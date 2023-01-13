from turtle import Turtle, Screen
from paddle import Paddles
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

s = Screen()
s.setup(width=800, height=600)
s.title("My Pong Game")
s.bgcolor("black")
s.tracer(0)
left_paddle = Paddles((-350, 0))
right_paddle = Paddles((350, 0))
ball = Ball()
board = ScoreBoard()
# Screen partition
for i in range(-300, 300):
    line = Turtle("square")
    line.shapesize(0.2, 0.2)
    line.penup()
    line.sety(i)
    line.color("white")
s.listen()
s.onkeypress(left_paddle.go_up, "Up")
s.onkeypress(left_paddle.go_down, "Down")
s.onkeypress(right_paddle.go_up, "w".lower())
s.onkeypress(right_paddle.go_down, "s".lower())

game_is_on = True
while game_is_on:
    s.update()
    ball.movement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with Paddle
    if ball.distance(right_paddle) < 55 and ball.xcor() > 320 or ball.distance(left_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        board.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        board.r_point()

    sleep(ball.move_speed)
s.exitonclick()
