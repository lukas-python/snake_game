from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.x_cor = 0
        self.y_cor = 0
        self.number_of_snake_body = 3
        self.snake_body = []

    def initializing_snake(self):
        for snake in range(self.number_of_snake_body):
            self.add_snake_segment(snake)

    def add_snake_segment(self, snake):
        new_snake = Turtle(shape='square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(self.x_cor, self.y_cor)
        self.x_cor -= 20
        self.snake_body.append(new_snake)

    def extend_snake(self):
        self.add_snake_segment(self.snake_body[-1].position())


    def moving_snake(self):
        for self.snake_segment in range(len(self.snake_body) - 1, 0, -1):
            self.new_x = self.snake_body[self.snake_segment - 1].xcor()
            self.new_y = self.snake_body[self.snake_segment - 1].ycor()
            self.snake_body[self.snake_segment].goto(self.new_x, self.new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)
