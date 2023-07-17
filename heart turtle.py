import turtle

t= turtle.Turtle()
s= turtle.Screen()
t.speed(1)
t.goto(0,-10)

s.bgcolor('black')
t.pensize(3)
t.color("red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)

t.setheading(60)
t.circle(-90,200)
t.forward(170)
t.end_fill()

t.speed(1)
t.hideturtle()
t.penup()
t.goto(-80,130)
t.speed(1)
t.color('white')
t.speed(1)
t.write("I",font=("verdana",20,"bold"))
t.goto(-50,130)
t.speed(1)
t.write("❤️",font=("verdana",20,"bold"))
t.goto(-10,130)
t.speed(1)
t.write("U",font=("verdana",20,"bold"))
t.goto(20,130)
t.speed(1)
t.write("BABY",font=("verdana",20,"bold"))

t.speed(10)
t.width(30)
t.pencolor("black")
t.penup()
t.goto(8,240)
t.pendown()

for broken in range(3):
    t.left(70)
    t.forward(50)
    t.right(65)
    t.forward(50)

t.speed (200)
t.hideturtle()
t.penup()
t.goto(-100,-120)
t.color('yellow')
t.write("TAPI BOHONG ",font=("italic",20,"bold"))

t.speed (200)
t.hideturtle()
t.penup()
t.goto(-30,-190)
t.write("😜",font=("verdana",40,"bold"))


t.pendown()
turtle.done()

