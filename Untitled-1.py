from turtle import *
import turtle

# Set up the screen to be fullscreen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=1.0, height=1.0)  # Fullscreen

# Initial turtle setup
setposition(-60, 0)
speed(0)
colors = ['yellow', 'red']
pensize(2)

# Drawing loop
for i in range(150):
    color(colors[i % 2])
    rt(i)
    circle(90, i)
    up()
    fd(i + 50)
    down()
    rt(90)
    fd(i - 65)

# Hide the turtle and finish drawing
hideturtle()
done()