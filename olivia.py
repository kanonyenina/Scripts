#creating the ugly face of olivia olele

import turtle

win = turtle.Screen()
win.title("Ugly Olivia by Awesome Nina")
win.bgcolor("white")
win.setup(width=1000, height=700)
win.tracer(0)


#face

face = turtle.Turtle()
face.speed(0)
face.shape("circle")
face.color("black") #cause she's a demon
face.shapesize(stretch_len=40, stretch_wid=30)
face.penup()
face.goto(0, 0)

# eyes
#first eye
eye_1 = turtle.Turtle()
eye_1.speed(0)
eye_1.shape("circle")
eye_1.color("red") #cause she's a demon
eye_1.shapesize(stretch_len=8, stretch_wid=4)
eye_1.penup()
eye_1.goto(-200, 100)
# second eye
eye_2 = turtle.Turtle()
eye_2.speed(0)
eye_2.shape("circle")
eye_2.color("red") #cause she's a demon
eye_2.shapesize(stretch_len=8, stretch_wid=4)
eye_2.penup()
eye_2.goto(200, 100)

while True:
    win.update()
