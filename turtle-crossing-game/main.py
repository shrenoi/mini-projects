import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossy")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car.create_car()
    car.move_car()

    #Increasing level and speed
    if player.at_start():
        score.increase_level()
        car.increase_speed()

    #Detect when player collides with car
    for cars in car.allcars:
        if player.distance(cars) < 20:
            game_is_on = False
            score.game_over()

    
screen.exitonclick()