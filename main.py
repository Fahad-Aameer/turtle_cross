import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()
screen.listen()
screen.onkey(turtle.move, 'Up')
score = Scoreboard()

game_is_on = True
no_of_loops = 6
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.new_car()
    for car in cars.cars:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False

    if turtle.ycor() > 300:
        turtle.refresh()
        cars.increase_speed()
        score.update_score()

screen.exitonclick()
