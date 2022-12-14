from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def counter_clockwise():
    tim.circle(100, 180)


def clockwise():
    tim.circle(-100, 180)


def clear_drawing():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward) #no parentheses when function as an input
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="e", fun=clockwise)
screen.onkey(key="q", fun=counter_clockwise)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()