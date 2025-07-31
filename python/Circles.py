import turtle
import random
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Circles.py")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

def draw_circle(x, y, radius, hue):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.color(rgb)
    
    t.circle(radius)
    
    if radius > 5:
        new_radius = radius * 0.8
        draw_circle(x, y, new_radius, (hue + 0.05) % 1.0)

def animate():
    t.clear()
    hue = (animate.hue + 0.005) % 1.0
    animate.hue = hue
    
    for _ in range(3):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        radius = random.randint(50, 150)
        draw_circle(x, y, radius, hue)
    
    screen.update()
    screen.ontimer(animate, 50)

animate.hue = 0.0
animate()
turtle.done()
