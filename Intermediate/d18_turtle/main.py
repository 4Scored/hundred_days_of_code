from turtle import Turtle, Screen
import random

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")

screen = Screen()
screen.colormode(255)

# dotted line
# for i in range(0,50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# different shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# random walk
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# for _ in range(250):
#     tim.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#     tim.forward(25)
#     tim.setheading(random.choice(directions))

# spirograph
# tim.pensize(5)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)

screen.exitonclick()