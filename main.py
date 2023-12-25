import turtle
import pandas as pd

TITLE = "Guess  the names of each US state"
PROMPT = "What's another state's name? "

data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# steps - get the input from answer_state and make it title case then check if it is in states.state

score = 0
wrong = 0
all_states = data.state.to_list()
game_is_on = True

while True:
    answer_state = screen.textinput(title=TITLE, prompt=PROMPT)
    if answer_state:
        answer_state = answer_state.title()
    else:
        game_is_on = False
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score  += 1
        answer_state = screen.textinput(title=f"Score {score} out of 50", prompt=PROMPT)
    else:
        wrong += 1
        if wrong  == 5:
            game_is_on = False
            break


screen.exitonclick()
