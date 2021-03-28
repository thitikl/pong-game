from turtle import Turtle
import random
heading = (90,270)

class Paddle(Turtle):
  def __init__(self, x_cor, y_cor):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid = 1, stretch_len = 5)
    self.penup()
    self.goto(x=x_cor, y=y_cor)
    self.setheading(random.choice(heading))
    self.speed(10)

  def pad_up(self):
    new_y = self.ycor()+20
    self.goto(self.xcor(),new_y)

  def pad_down(self):
    new_y = self.ycor()-20
    self.goto(self.xcor(),new_y)

  def auto_move(self):
    self.forward(10)

