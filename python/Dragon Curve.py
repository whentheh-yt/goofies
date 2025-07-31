import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dragon Curve.py")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.width(2)

def dragon_curve(order, length, hue=0.0, direction=1):
    if order == 0:
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.color(rgb)
        t.forward(length)
    else:
        hue = (hue + 0.02) % 1.0  # Shift color
        t.left(45 * direction)
        dragon_curve(order - 1, length / (2 ** 0.5), hue, 1)
        t.right(90 * direction)
        dragon_curve(order - 1, length / (2 ** 0.5), hue, -1)
        t.left(45 * direction)

t.penup()
t.goto(-150, 0)
t.pendown()

order = 16
dragon_curve(order, 500)

screen.update()
turtle.done()