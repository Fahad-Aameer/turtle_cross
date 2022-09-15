import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_number = random.randint(0, 6)
        if random_number == 1:
            car = Turtle()
            car.penup()
            car.shape('square')
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.right(180)
            car_y = random.randint(-250, 250)
            car.goto(350, car_y)
            self.cars.append(car)

    def move(self):
        for i in self.cars:
            i.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
