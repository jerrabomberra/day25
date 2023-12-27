import turtle
import pandas as pd

TITLE = "Guess  the names of each US state"
PROMPT = "What's another state's name? "
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt=PROMPT)
    if answer_state:
        answer_state = answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif answer_state == "Exit":
        # new_list = list(set(all_states).difference(guessed_states)
        education = pd.DataFrame(set(all_states).difference(guessed_states))

        education.to_csv("states_to_learn.csv")
        break

# states_to_learn.csv
