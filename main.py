from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

TOP_BORDER = 240
BOTTOM_BORDER = -240
RIGHT_BORDER = 330
LEFT_BORDER = -330

screen = Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.screensize(800, 600)
screen.tracer(0)

com = Paddle(350,0)
user = Paddle(-350,0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(user.pad_up, "w")
screen.onkey(user.pad_down, "s")
screen.onkey(com.pad_up, "Up")
screen.onkey(com.pad_down, "Down")

game_on = True
while game_on:
  screen.update()

  #bounce with the wall
  if ball.ycor() > TOP_BORDER or ball.ycor() < BOTTOM_BORDER:
    ball.bounce_wall()
  
  #bounce with right paddle
  if ball.distance(com) < 50 and ball.xcor() > RIGHT_BORDER:
    ball.bounce_paddle()
    ball.increase_speed()
  
  #bounce with left paddle
  if ball.distance(user) < 50 and ball.xcor() < LEFT_BORDER:
    ball.bounce_paddle()
    ball.increase_speed()

  #set auto move for computer paddle
  if com.ycor() > (TOP_BORDER-50) or com.ycor() < (BOTTOM_BORDER+50):
    new_heading = com.heading() * -1
    com.setheading(new_heading)
  
  #check game end condition
  if ball.xcor() > (RIGHT_BORDER+40):
    ball.reset()
    score.clear()
    score.user_score += 1
    score.show_score()

  if ball.xcor() < (LEFT_BORDER-40):
    ball.reset()
    score.clear()
    score.com_score += 1
    score.show_score()

  ball.move()
  # com.auto_move()
  time.sleep(0.05)

