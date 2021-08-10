import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
game_over = GameOver()

player = Player()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
all_cars = []
run_times = 0
while game_is_on:
    time.sleep(0.1)
    if run_times % 6 == 0:
        new_car = CarManager()
        all_cars.append(new_car)
    screen.update()
    for car in all_cars:
        car.move()
    for car in all_cars:
        if car.distance(player) < 15:
            game_is_on = False
    run_times += 1
    if player.restart():
        player.reset()
        player.create_turtle()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        score_board.run_times += 1
        score_board.writing()

game_over.end_game()
screen.exitonclick()
