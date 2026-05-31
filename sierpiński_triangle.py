import turtle
import random

n = 1000
t = turtle.Turtle()
screen = turtle.Screen()
A = (0, 0)
B = (200, 0)
C = (100, 173)

vertices = [A, B, C]

curr_point = [100,50]
t.penup(); t.goto(A); t.pendown()
for p in [B, C, A]:
    t.goto(p)
for _ in range(n):
    next_vertex = random.choice(vertices)
    curr_point[0] = (curr_point[0] + next_vertex[0]) / 2
    curr_point[1] = (curr_point[1] + next_vertex[1]) / 2
    t.penup()
    t.goto(curr_point)
    t.dot(3, "blue")
screen.update()
turtle.done()