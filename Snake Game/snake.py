from turtle import Turtle
xy_starting = [(-20, 0), (-40, 0)]
move_by_forward = 20
# Hardcoding Headings for easy readability
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
# In case we want to tweak the game
# Just look at the constants and change accordingly

class Snake:
    def __init__(self):
        # What should happen when we initialize a new snake object
        my_turtle_1 = Turtle("triangle")
        my_turtle_1.color("green")
        self.turtles = [my_turtle_1]
        self.head = self.turtles[0]
        self.create_snake()

    def create_snake(self):
        for coordinates in xy_starting:
            my_turtle = Turtle("square")
            my_turtle.color("green")
            my_turtle.penup()  # to
            my_turtle.goto(coordinates)
            self.turtles.append(my_turtle)
            #Simply appends other turtles passed to the turtles list
            # Changing the positioning of the second and third box otherwise
            # they end up on top of each other

    def add_turtle(self, coordinates):
        my_turtle = Turtle("square")
        my_turtle.color("green")
        my_turtle.penup()  # to
        my_turtle.goto(coordinates)
        self.turtles.append(my_turtle)

    def extend(self):
        #catches the tail of the snake and inserts a turtle there
        self.add_turtle(self.turtles[-1].position())


    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            # Simply start = 2, stop = 0, step = -1
            # to goto a particular x and y position
            x_coord = self.turtles[turtle - 1].xcor()  # go to the last turtle
            y_coord = self.turtles[turtle - 1].ycor()
            # turtles[turtle].penup()
            self.turtles[turtle].goto(x_coord, y_coord)
        self.turtles[0].penup()  # To not make drawing a line when moving
        self.turtles[0].forward(move_by_forward)

    def up(self):
        # If the turtle goes up it shouldn't be going down by pressing down arrow
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # If the turtle goes down it shouldn't be going up by pressing up arrow
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # If the turtle goes right it shouldn't be going left by pressing left arrow
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # If the turtle goes left it shouldn't be going right by pressing right arrow
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

