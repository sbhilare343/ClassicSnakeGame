from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen setup.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Slytherin")
screen.tracer(0)

snake = Snake()  #
food = Food()  #
scoreboard = ScoreBoard()  #

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # To update each frame to avoid delay.
    screen.update()
    time.sleep(0.1)
    snake.move()  #

    # Detect collision with food.
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.home()
        snake.reset_seg()

    # # Detect collision with tail.
    # for segment in snake.segments:
    #     if segment != snake.head:
    #         if snake.head.distance(segment) < 10:
    #             game_is_on = False
    #             scoreboard.game_is_over()
    # # If head collide with any segment in the tail.
    # # Trigger game over.

    # # Using slicing.
    lists = snake.segments[1:]
    for segment in lists:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.home()
            snake.reset_seg()

screen.exitonclick()
