from turtle import Turtle
TOP_EDGE = 310
BOTTOM_EDGE = -310
MOVE_DISTANCE = 60


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up_paddle(self):
        y_axis = self.ycor()
        if y_axis < TOP_EDGE:
            new_position = (self.xcor(), y_axis + MOVE_DISTANCE)
            self.goto(new_position)

    def down_paddle(self):
        y_axis = self.ycor()
        if y_axis > BOTTOM_EDGE:
            new_position = (self.xcor(), y_axis - MOVE_DISTANCE)
            self.goto(new_position)

    def restart(self, position):
        self.goto(position)
