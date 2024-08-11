from turtle import Turtle
import random
draw= Turtle()

colours = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black"]
direction = [0,90,180,270]
draw.pensize(10)
draw.speed("fastest")

for i in range (200):
    draw.color(random.choice(colours))
    draw.forward(30)
    draw.setheading(random.choice(direction))
