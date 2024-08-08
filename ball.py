from turtle import Turtle, Screen

screen = Screen()

y_dep = 15


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.player1_score = 0
        self.player2_score = 0
        # another way to do that is to create a function to bounce the ball and create an attribute with the intensity of dx and dy

    def move_ball(self, d):
        x_new = self.xcor() + d[0]
        y_new = self.ycor() + d[1]
        self.goto(x_new, y_new)
        if self.ycor() >= 280:
            d[1] = -15
        elif self.ycor() <= -280:
            d[1] = 15

    def off_limit(self, d):
        if self.xcor() > 410:
            d[0] *= -1
            self.player1_score += 1
            return True
        elif self.xcor() < -410:
            d[0] *= -1
            self.player2_score += 1
            return True
