from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.penup()
        self.color("white")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def restart(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
