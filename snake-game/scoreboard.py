from turtle import Turtle, Screen
STYLE = ("Courier", 15)
ALIGNMENT = "center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", font=STYLE, align= ALIGNMENT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=STYLE, align= ALIGNMENT)