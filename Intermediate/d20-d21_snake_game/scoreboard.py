from turtle import Turtle

ALIGHNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()    

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGHNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):        
        if self.score > self.high_score:
            self.high_score = self.score        
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGHNMENT, font=FONT)