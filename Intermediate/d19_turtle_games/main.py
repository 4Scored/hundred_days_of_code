from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = [-70, -40, -10, 20, 50, 80]
for t_idx in range(0,6):
    turt = Turtle("turtle")
    turt.color(colors[t_idx])
    turt.penup()
    turt.goto(x=-220, y=y_pos[t_idx])
    all_turtles.append(turt)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()            
            if winning_color == user_bet:
                print("You've chosen correctly and won!")
            else:
                print("You've chosen wrong and lost...")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()

'''
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.setheading(tim.heading() + 10)

def move_right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
'''