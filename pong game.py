#creating a pong game 

import turtle

win = turtle.Screen()
win.title("Awesome Pong by Nina")
win.bgcolor("pink")
win.setup(width=800, height=600)
win.tracer(0)

#score
score_a = 0
score_b = 0

#paddle A
hit_em_up_a = turtle.Turtle()
hit_em_up_a.speed(0)
hit_em_up_a.shape("square")
hit_em_up_a.color("red")
hit_em_up_a.shapesize(stretch_wid=5, stretch_len=1)
hit_em_up_a.penup()
hit_em_up_a.goto(-350, 0)

#paddle b
hit_em_up_b = turtle.Turtle()
hit_em_up_b.speed(0)
hit_em_up_b.shape("square")
hit_em_up_b.color("red")
hit_em_up_b.shapesize(stretch_wid=5, stretch_len=1)
hit_em_up_b.penup()
hit_em_up_b.goto(350, 0)


#ball
deez_nuts = turtle.Turtle()
deez_nuts.speed(0)
deez_nuts.shape("square")
deez_nuts.color("red")
deez_nuts.penup()
deez_nuts.goto(0, 0)
deez_nuts.dx = .3
deez_nuts.dy = -.3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#creating a function to move the objects
def hit_em_up_a_up():
    y = hit_em_up_a.ycor()
    y += 20 
    hit_em_up_a.sety(y)
#now we need to call the function

def hit_em_up_a_down():
    y = hit_em_up_a.ycor()
    y -= 20 
    hit_em_up_a.sety(y)


def hit_em_up_b_up():
    y = hit_em_up_b.ycor()
    y += 20 
    hit_em_up_b.sety(y)
#now we need to call the function

def hit_em_up_b_down():
    y = hit_em_up_b.ycor()
    y -= 20 
    hit_em_up_b.sety(y)

win.listen()
win.onkeypress(hit_em_up_a_up, "w")
win.onkeypress(hit_em_up_a_down, "s")
win.onkeypress(hit_em_up_b_up, "Up")
win.onkeypress(hit_em_up_b_down, "Down")

#main game loop
while True:
    win.update()
    #move deez nuts
    deez_nuts.setx(deez_nuts.xcor() + deez_nuts.dx)
    deez_nuts.sety(deez_nuts.ycor() + deez_nuts.dy)

    #add borders
    if deez_nuts.ycor() > 290:
        deez_nuts.sety(290)
        deez_nuts.dy *= -1

    if deez_nuts.ycor() < -290:
        deez_nuts.sety(-290)
        deez_nuts.dy *= -1

    if deez_nuts.xcor() > 390:
        deez_nuts.goto(0, 0)
        deez_nuts.dx *= -1
        score_a += 1
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if deez_nuts.xcor() < -390:
        deez_nuts.goto(0, 0)
        deez_nuts.dx *= -1
        score_b += 1
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #ball colliding with paddle
    if (deez_nuts.xcor() > 340 and deez_nuts.xcor() < 350) and (deez_nuts.ycor() < hit_em_up_b.ycor() + 40 and deez_nuts.ycor() > hit_em_up_b.ycor() -40):
        deez_nuts.setx(340)
        deez_nuts.dx *= -1

    if (deez_nuts.xcor() < -340 and deez_nuts.xcor() > -350) and (deez_nuts.ycor() < hit_em_up_a.ycor() + 40 and deez_nuts.ycor() > hit_em_up_a.ycor() -40):
        deez_nuts.setx(340)
        deez_nuts.dx *= -1