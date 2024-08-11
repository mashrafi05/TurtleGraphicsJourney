from turtle import Turtle, Screen
import random
tim = Turtle()

colors=["darkblue","darkcyan","darkred","dodgerblue","gold","hotpink","maroon","yellow","yellowgreen","violet"]
def shape(num):
    angle= 360/num
    for x in range(num):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random.choice(colors))
    shape(i)
screen = Screen()
screen.exitonclick()
