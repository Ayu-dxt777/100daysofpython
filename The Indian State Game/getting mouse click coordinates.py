#gets the coordinates of the mouse where it is clicked
import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("India States Game")
image = "India-locator-map-blank.gif"
screen.addshape(image)
turtle.shape(image)

def mouse_click_coords(x ,y):
    print(x, y)

# onscreenclick is an event listener
turtle.onscreenclick(mouse_click_coords)
turtle.mainloop()
# A way to keep our screen open even if the code is finished
