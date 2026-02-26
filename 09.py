import turtle, colorsys

t, s = turtle.Turtle(), turtle.Screen()
s.bgcolor('#000000')
s.colormode(255)
t.speed(100)

for n in range(10):
    r, g, b = colorsys.hsv_to_rgb(0.0, n*0.1, 1.0 - n*0.02)
    rgb = tuple(int(c*255) for c in (r,g,b))
    t.pencolor('white' if n==0 else rgb)
    t.pensize(2 + n*0.2)
    for x in range(8):
        t.speed(x+10)
        [t.circle(80+n*20, 90) or t.lt(90) for _ in range(2)]
        t.lt(45)

turtle.done()