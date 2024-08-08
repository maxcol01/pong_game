from turtle import Turtle


class Score(Turtle):
    def __init__(self, player_score, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(f"{player_score}", align="center",font=("Courier", 80, "normal"))
        self.hideturtle()



