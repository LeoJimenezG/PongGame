from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=-170, y=320)
        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score_left}     {self.score_right}", font=("Courier", 60, "normal"))

    def point_left(self):
        self.score_left += 1

    def point_right(self):
        self.score_right += 1
