from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.hideturtle()
    self.penup()
    self.com_score = 0
    self.user_score = 0
    self.goto(0,120)
    self.write(f"{self.user_score} | {self.com_score}", align = "center", font = ("Arial", 60, "normal") )

  def show_score(self):
    self.write(f"{self.user_score} | {self.com_score}", align = "center", font = ("Arial", 60, "normal") )