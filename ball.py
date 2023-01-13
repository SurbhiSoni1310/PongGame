from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.001

    def movement(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.00000001

    def reset_position(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.001


