from turtle import Turtle, Screen
STYLE = ("Courier", 15)
ALIGNMENT = "center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            hs = file.read()
        self.highscore = int(hs)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", font=STYLE, align= ALIGNMENT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", font=STYLE, align= ALIGNMENT)
