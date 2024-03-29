from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Pro Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
snake.initializing_snake()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.moving_snake()

    #Detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.increse_score()

    #Detect collision with wall

    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with snake body
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
