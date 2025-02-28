from turtle import *
import random

speed('fast')
hideturtle()

def grow(length, decrease, angle, noise = 0):

    if length > 10:
        
        width(length / 10)
        forward(length)

        new_length = length * decrease

        if noise > 0:
            new_length *= random.uniform(0.9, 1.1)

        angle_left = angle + random.gauss(0, noise)
        angle_right = angle + random.gauss(0, noise)

        left(angle_left)
        grow(new_length, decrease, angle, noise)
        right(angle_left)

        right(angle_right)
        grow(new_length, decrease, angle, noise)
        left(angle_right)

        backward(length)

penup()
goto(0, -400)
pendown()
left(90)

tracer(1000)
grow(150, 0.8, 24, 10)

tracer(True)
exitonclick()