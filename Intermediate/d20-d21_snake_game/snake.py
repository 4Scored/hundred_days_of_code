from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]     

    # snake initialization
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): # movement, tail-end of snake moves first
            prev_x = self.segments[seg_num - 1].xcor()
            prev_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(prev_x, prev_y)
        self.head.forward(MOVE_DIST) 

    def add_segment(self, pos):
        turt = Turtle("square")
        turt.color("white")
        turt.penup()
        turt.goto(pos)
        self.segments.append(turt)

    def extend(self):
        self.add_segment(self.segments[-1].position()) # added segment to last segment 

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear() # remove all segments
        self.create_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
