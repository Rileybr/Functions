import turtle

side_length = float(input("What is the side length?: "))
cross_color = input("What color are the crosses?: ")


def draw_cross():
    turtle.pendown()
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(side_length)
        turtle.left(90)
        turtle.forward(side_length)
        turtle.right(90)
        turtle.forward(side_length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def main():
    turtle.color(cross_color)
    # draws center cross
    turtle.goto(0, 0)
    draw_cross()
    # draws right cross
    turtle.goto((side_length * 3), 0)
    draw_cross()
    # draws left cross
    turtle.goto((side_length * -3), 0)
    draw_cross()
    # draws top cross
    turtle.goto(0, (side_length * 3))
    draw_cross()
    # draws bottom cross
    turtle.goto(0, (side_length * -3))
    draw_cross()
    turtle.exitonclick()

main()
