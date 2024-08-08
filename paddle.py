from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(x, y)
        # self.x_pos = x
        # self.y_pos = y

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 10)
