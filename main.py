import turtle
import pandas

screen = turtle.Screen()
screen.title("Usa state game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What is other state name?").title()

    if answer_state == "Exit":
        missing_states = [ states for states in all_states if states not in guessed_states ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break



#    if answer_state == "Exit":
#        missing_states = []
#        for state in all_states:
#            if state not in guessed_states:
#                missing_states.append(state)
#        new_data = pandas.DataFrame(missing_states)
#        new_data.to_csv("States_to_learn.csv")
#        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        State_data = data[data.state == answer_state]
        t.goto(int(State_data.x),int(State_data.y))
        t.write(State_data.state.item())

screen.exitonclick()





