from turtle import Turtle


class Paddle(Turtle):
    """Class for paddle appearance and behavior."""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        """Method for moving paddle up."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Method for moving paddle down."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
