import turtle as t


def isReset():
    t.reset()

def Move_left():
    t.stamp()
    t.setheading(180)
    t.forward(50)

def Move_right():
    t.stamp()
    t.setheading(0)
    t.forward(50)

def Move_down():
    t.stamp()
    t.setheading(-90)
    t.forward(50)

def Move_up():
    t.stamp()
    t.setheading(90)
    t.forward(50)

def Run():
    t.shape("turtle")

    t.onkey(isReset, 'Escape')
    t.onkey(Move_down, 's')
    t.onkey(Move_up, 'w')
    t.onkey(Move_right, 'd')
    t.onkey(Move_left, 'a')

    t.listen()

    t.exitonclick()



t.speed(100)
Run()