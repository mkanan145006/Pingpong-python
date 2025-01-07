import turtle as t

window = t.Screen()
window.title("simple game by xkananx")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Left
left = t.Turtle()
left.speed(0)
left.shape("square")
left.shapesize(stretch_wid=5, stretch_len=0.7)
left.color("lime")
left.penup()
left.goto(-360, 0)

# Right
right = t.Turtle()
right.speed(0)
right.shape("square")
right.shapesize(stretch_wid=5, stretch_len=0.7)
right.color("lime")
right.penup()
right.goto(360, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("grey")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# pen
penr=t.Turtle()
penr.speed(0)
penr.penup()
penr.hideturtle()
penr.goto(360,260)
penr.color("white")
penr.write(0,align="center",font=("Courier,",30,"normal"))

penl=t.Turtle()
penl.speed(0)
penl.penup()
penl.hideturtle()
penl.goto(-360,260)
penl.color("white")
penl.write(0,align="center",font=("Courier,",30,"normal"))

penm=t.Turtle()
penm.speed(0)
penm.penup()
penm.hideturtle()
penm.goto(0,150)
penm.color("white")

# funx
def left_up():
    y=left.ycor()
    if y <240 :
        y+=20
    left.sety(y)
def left_down():
    y=left.ycor()
    if y >-240 :
        y-=20
    left.sety(y)
def right_up():
    y=right.ycor()
    if y <240 :
        y+=20
    right.sety(y)
def right_down():
    y=right.ycor()
    if y >-240 :
        y-=20
    right.sety(y)

# keybinds
window.listen()
window.onkeypress(left_up, "w")
window.onkeypress(left_down, "s")
window.onkeypress(right_up, "Up")
window.onkeypress(right_down, "Down")


def game():
    rightscore = 0
    leftscore = 0
    while True:
        
        window.update()

        # ball movement
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        # borders
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Goal!
        if ball.xcor() > 390:
            ball.goto(0, 0)
            leftscore+=1
            penl.clear()
            penl.write(leftscore, align="center", font=("Courier,", 30, "normal"))
            ball.dx *= -1
        if ball.xcor() < -390:
            ball.goto(0, 0)
            rightscore+=1
            penr.clear()
            penr.write(rightscore, align="center", font=("Courier,", 30, "normal"))
            ball.dx *= -1

        # Save!
        if (ball.xcor()>350 and ball.xcor()<360) and (ball.ycor()<right.ycor()+50 and ball.ycor()>right.ycor()-50):
            ball.setx(350)
            ball.dx*=-1
        if (ball.xcor()<-350 and ball.xcor()>-360) and (ball.ycor()<left.ycor()+50 and ball.ycor()>left.ycor()-50):
            ball.setx(-350)
            ball.dx*=-1

        #end of the game
        if rightscore==5 or leftscore==5:
            penm.write("We have a WINNER!!!", align="center", font=("Courier,", 50, "normal"))
            rightscore = 0
            leftscore = 0
            break
game()
