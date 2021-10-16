import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("India States Game")
image = "India-locator-map-blank.gif"
screen.addshape(image)

turtle.shape(image)
india_dataset = pd.read_csv("India Coords turtle.csv")
india_dataset = india_dataset.rename(columns = {'X ':'X'})
# Added white space causes issues
guessed_states = []
states_not_guessed = []

while len(guessed_states) < 38:
    all_states = india_dataset.State.to_list()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States Correct", prompt="What's the state's name?").title()

    if answer_state == "Exit":
        states_not_guessed = list(set(all_states) - set(guessed_states))
        states_to_learn_dataframe = pd.DataFrame(states_not_guessed, columns=['States to learn'])
        states_to_learn_dataframe.to_csv('States not guessed need to learn-2.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        writing_turtle = turtle.Turtle()
        writing_turtle.hideturtle()
        writing_turtle.penup()
        answered_state_Date_row = india_dataset[india_dataset.State == answer_state]
        writing_turtle.goto(int(answered_state_Date_row.X), int(answered_state_Date_row.Y))
        writing_turtle.write(answer_state)

