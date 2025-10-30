import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "intermediate/25_us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)
    
states_data = pandas.read_csv("intermediate/25_us_states_game/50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 Sates Correct",
                                    prompt="What's another state's name?")
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("intermediate/25_us_states_game/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(state_data.state.item())