from turtle import Turtle
import random

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.setheading(random.randint(1,359))
    self.x_move = 5
    self.y_move = 5

  #define automatic move of the ball
  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  #bounce against the top and bottom wall
  def bounce_wall(self):
    self.y_move *= -1

  #bounce against paddle
  def bounce_paddle(self):
    self.x_move *= -1

  def increase_speed(self):
    if self.x_move > 0:
      self.x_move += 1
    else:
      self.x_move -= 1
    
    if self.y_move > 0:
      self.y_move += 1
    else:
      self.y_move -= 1

  def reset(self):
    self.goto(0,0)
    self.bounce_paddle()
    self.x_move = 5
    self.y_move = 5
