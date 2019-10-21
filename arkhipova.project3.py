#построение фигуры с помощью цикла for
import turtle

ANIMATION_SPEED = 0
COLORS = ['red', 'purple', 'blue', 'green']

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

def sq(a):
    for i in range(4):
        turtle.color(COLORS[i%4])
        turtle.forward(a)
        turtle.left(90)

b = 50

for i in range(60):
    sq(b)
    turtle.right(10)
    b = b+5
turtle.done()