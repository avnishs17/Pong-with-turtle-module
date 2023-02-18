from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")

screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	# Detect collision with up or down wall

	if ball.ycor() > 280 or ball.ycor() < -285:
		ball.bounce_y()

	# Detect collision with the paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
		ball.bounce_x()

	# Detect when right paddle misses
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.l_point()

	# Detect when right paddle misses
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.r_point()
screen.exitonclick()
