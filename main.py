from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


DISTNCE_TO_SCORE = 15
DISTNCE_TO_LOSE = 290


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food
    if snake.head.distance(food) < DISTNCE_TO_SCORE:
        food.refresh()
        score.score_up()
        snake.grow()

    #detecting collision with wall
    if abs(snake.head.xcor())>DISTNCE_TO_LOSE or abs(snake.head.ycor())>DISTNCE_TO_LOSE:
        score.game_over()
        game_is_on = False

    #detecting collision with tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            score.game_over()
            game_is_on = False




screen.exitonclick()