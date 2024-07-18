from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(starting_position)

    def paddle_up(self):
        if self.ycor() >= 250:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        if self.ycor() <= -250:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

