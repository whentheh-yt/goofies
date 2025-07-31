import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Spiral.py")

spiral = turtle.Turtle()
spiral.speed(0)  # Fastest speed
spiral.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    spiral.pencolor(colors[i % len(colors)])
    spiral.forward(i * 0.5)
    spiral.left(59)
    
spiral.hideturtle()
turtle.done()