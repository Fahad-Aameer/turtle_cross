from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Score: {self.my_score}", align="center", font=FONT)

    def update_score(self):
        self.my_score += 1
        self.clear()
        self.write(f"Score: {self.my_score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=("Courier", 30, "bold"))
