COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        self.allcars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 250)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.allcars.append(new_car)

    def move_car(self):
        for cars in self.allcars:
            cars.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

      

