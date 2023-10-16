from turtle import Turtle

ALIGNMENT = "center"
FONT = ["Courier", 14, "normal"]


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        with open("prevScore.txt", "r+") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.write(f"Score:{self.score} HighScore:{self.high_score}", align=ALIGNMENT, font=FONT, move=False)

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} HighScore:{self.high_score}", align=ALIGNMENT, font=FONT, move=False)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("prevScore.txt", "r+") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_is_over(self):
    #     self.hideturtle()
    #     self.home()
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT, move=False)

    def increase_score(self):
        self.score += 1
        self.update()

