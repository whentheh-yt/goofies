import turtle
import random
import math
import time

screen = turtle.Screen()
screen.bgcolor("midnightblue")
screen.title("Fractal Tree.py")
screen.tracer(0) 

stars = turtle.Turtle()
stars.hideturtle()
stars.penup()
stars.color("white")

for _ in range(100):
    x = random.randint(-screen.window_width()//2, screen.window_width()//2)
    y = random.randint(-screen.window_height()//2, screen.window_height()//2)
    size = random.uniform(0.5, 3)
    stars.goto(x, y)
    stars.dot(size)

fireflies = []
for _ in range(20):
    fly = turtle.Turtle()
    fly.shape("circle")
    fly.shapesize(0.3)
    fly.color("gold")
    fly.penup()
    fly.speed(0)
    fly.goto(random.randint(-200, 200), random.randint(-100, 300))
    fireflies.append(fly)

tree = turtle.Turtle()
tree.speed(0)
tree.width(2)
tree.color("forestgreen")
tree.left(90)
tree.penup()
tree.goto(0, -250)
tree.pendown()

def draw_branch(length, angle):
    if length < 5:  # Base case (leaf)
        tree.color("limegreen")
        tree.dot(3)
        tree.color("forestgreen")
        return
    
    tree.pendown()
    tree.forward(length)
    
    # Left branch
    tree.left(angle)
    draw_branch(length * 0.7, angle * 0.9)
    tree.right(angle)
    
    # Right branch
    tree.right(angle)
    draw_branch(length * 0.7, angle * 0.9)
    tree.left(angle)
    
    tree.penup()
    tree.backward(length)

draw_branch(100, 30)

def move_fireflies():
    for fly in fireflies:
        fly.goto(
            fly.xcor() + random.uniform(-2, 2),
            fly.ycor() + random.uniform(-0.5, 1.5)
        )
        
        # Wrap around screen edges
        if abs(fly.xcor()) > screen.window_width()//2:
            fly.setx(-fly.xcor() * 0.9)
        if fly.ycor() > screen.window_height()//2:
            fly.sety(-screen.window_height()//4)
    
    screen.update()
    screen.ontimer(move_fireflies, 50)

move_fireflies()
turtle.done()