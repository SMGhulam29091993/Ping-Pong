from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
