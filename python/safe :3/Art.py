import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Art.py")

artist = turtle.Turtle()
artist.speed(0)
artist.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "cyan", "magenta"]

def draw_spiral():
    size = random.randint(10, 100)
    angle = random.randint(5, 30)
    artist.color(random.choice(colors))
    for i in range(size):
        artist.forward(i * 2)
        artist.right(angle)

def draw_star():
    points = random.randint(5, 12)
    length = random.randint(20, 100)
    artist.color(random.choice(colors))
    angle = 180 - (180 / points)
    artist.begin_fill()
    for i in range(points):
        artist.forward(length)
        artist.right(angle)
    artist.end_fill()

def draw_crazy_shape():
    sides = random.randint(3, 10)
    length = random.randint(10, 50)
    artist.color(random.choice(colors))
    artist.begin_fill()
    for _ in range(sides):
        artist.forward(length)
        angle = random.randint(60, 170)
        artist.right(angle)
    artist.end_fill()

def draw_circle_pattern():
    circles = random.randint(5, 15)
    radius = random.randint(10, 50)
    artist.color(random.choice(colors))
    for _ in range(circles):
        artist.circle(radius)
        artist.right(360 / circles)

def move_random():
    artist.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    artist.goto(x, y)
    artist.pendown()

for _ in range(15):
    move_random()
    shape_type = random.randint(1, 4)
    if shape_type == 1:
        draw_spiral()
    elif shape_type == 2:
        draw_star()
    elif shape_type == 3:
        draw_crazy_shape()
    else:
        draw_circle_pattern()

artist.hideturtle()
screen.mainloop()
