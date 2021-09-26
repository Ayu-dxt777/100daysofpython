from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
#giving keyword arguments here for better understanding
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #Screen wont refresh
# First step is to creat a snake


# Incorporating Event Listeners
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
snake_moves = True
# Snake moves
while snake_moves:
    screen.update() #move all three blocks at once
    time.sleep(0.1)
    snake.move()

    ## DETECTING COLLISION WITH FOOD
    ## Detecting collision by using distance method
    ## Checking the distance of the snake from the food
    ## We know that food is 10 by 10 in dimensions
    ## After testing 15 was the best one
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    ## DETECTING COLLISION WITH WALL

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake_moves = False
        scoreboard.game_over()
        ## Game ends

    ## DETECT COLLISION WITH TAIL
    for turtle in snake.turtles:
        if turtle == snake.head:
            pass
        elif snake.head.distance(turtle) < 10:
            snake_moves = False
            scoreboard.game_over()

        # Another way by using list slicing
    # for turtle in snake.turtles[1:]:
    #     if snake.head.distance(turtle) < 10:
    #         snake_moves = False
    #         scoreboard.game_over()

    ## If head collides with any segment in the tail
    # Trigger Game over


screen.exitonclick()
