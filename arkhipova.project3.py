#построение фигуры с помощью цикла for
import turtle

ANIMATION_SPEED = 0
COLORS = ['red', 'purple', 'blue', 'green']
size = 50

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

def sq(a):
    for i in range(4):
        turtle.color(COLORS[i%4])
        turtle.forward(a)
        turtle.left(90)

for i in range(60):
    sq(size)
    turtle.right(10)
    size = size+5
turtle.done()