from turtle import Turtle
import random as random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.x_location = 260
        self.create_car()

    def create_car(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.right(180)
        self.location()

    def location(self):
        y_location = random.randint(-240, 240)
        self.goto(x=self.x_location, y=y_location)

    def move(self):
        self.fd(STARTING_MOVE_DISTANCE)
