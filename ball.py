from turtle import Turtle


class Ball(Turtle):
    """Class for paddle appearance and behavior."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Method to move ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Method to bounce the ball in the y direction."""
        self.y_move *= -1

    def bounce_x(self):
        """Method to bounce the ball in the x direction."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Method to reset ball to center of screen and change serving direction when paddle misses."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
