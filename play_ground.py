from turtle import Turtle


class PlayGround(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(x=0, y=-450)
        #  by puttin this like that I apply the draw_line() function onto the object (the same object) so I move it !
        #  if I want to create several instance I need to create several object !
        self.draw_line()

    def draw_line(self):
        """This is a function that allows an object onto which the function is applied to move vertically from a
        starting position"""
        y_pos = -450
        for _ in range(20):
            self.goto(x=0, y=y_pos)
            y_pos += 20
