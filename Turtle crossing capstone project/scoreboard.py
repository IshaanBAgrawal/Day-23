from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(x=-210, y=260)
        self.run_times = 1
        self.writing()

    def writing(self):
        self.clear()
        self.write(arg=f"Level: {self.run_times}", align="center", font=FONT)


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)

    def end_game(self):
        self.write(arg="Game Over.", align="center", font=FONT)

    def exit(self):
        self.goto(0, 280)
        self.write(arg="Click anywhere on the screen to exit.", align="center", font=FONT)
