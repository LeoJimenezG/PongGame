from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_distance = 10
        self.y_distance = 10
        self.move_speed = 0.1

    def restart(self):
        self.goto(x=0, y=0)
        self.bounce_x()
        self.x_distance = 15
        self.y_distance = 15
        self.move_speed = 0.1

    def move(self):
        x_axis = self.xcor() + self.x_distance
        y_axis = self.ycor() + self.y_distance
        self.goto(x_axis, y_axis)

    def bounce_y(self):
        self.y_distance *= -1

    def bounce_x(self):
        self.x_distance *= -1
        self.move_speed *= 0.9
