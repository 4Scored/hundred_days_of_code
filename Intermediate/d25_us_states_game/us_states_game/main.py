import pandas as pd
import turtle

IMG = "blank_states_img.gif"
df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("50 U.S. States Game")
screen.addshape(IMG)
turtle.shape(IMG)

states = df.state.to_list()
states_guessed = []

while len(states_guessed) < 50:    
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States", prompt="What's another State's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in states_guessed]
        # for state in states:
        #     if state not in states_guessed:
        #         missing_states.append(state)
        missed_states_df = pd.DataFrame(missing_states)
        missed_states_df.to_csv("missed_states.csv")
        break
    if answer_state in states and answer_state not in states_guessed:
        states_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()        
        state_x_cor = df[df["state"] == answer_state]["x"].item()
        state_y_cor = df[df["state"] == answer_state]["y"].item()
        t.goto(int(state_x_cor), int(state_y_cor)) 
        t.write(answer_state)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop() # screen.exitonclick()