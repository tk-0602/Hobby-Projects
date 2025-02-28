# Inspired by https://www.youtube.com/watch?v=kMBj2fp52tA

from turtle import *
import random

speed('fastest')
hideturtle()

def euler_curve(step_size, angle_step, n_steps):
    angle  = 0
    for i in range(n_steps):
        right(angle)
        forward(step_size)
        angle += angle_step

    print("Done")

tracer(100)
euler_curve(step_size = 2, angle_step = 1.01, n_steps = 100000)

tracer(True)
exitonclick()