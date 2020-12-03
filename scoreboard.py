from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    """Class for scoreboard apperance and behavior."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Method to write to scoreboard."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Method for updating left player score."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Method for updating right player score."""
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
