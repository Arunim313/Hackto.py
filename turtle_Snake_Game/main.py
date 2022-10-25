from turtle import Screen, Turtle, distance, position
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset( )
    
    # Detect collision with tail
    for segment in snake.segment[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.game_over()
            snake.reset
        
         
 
screen.exitonclick()