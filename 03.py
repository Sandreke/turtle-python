from turtle import *

speed(0)
bgcolor("black")
setheading(45)

for i in range(235):
    color('#ff8fab')
    circle(270-i,90), lt(90)
    circle(270-i,90), lt(18)

mainloop()