import turtle

def main():
    draw_square()


def draw_square(size_square=50,
                number_squar=10,
                step=30):
    turtle.shape('turtle')
    for i in range(number_squar):
        for i in range(4):
            turtle.forward(size_square)
            turtle.left(90)
        turtle.penup()
        turtle.forward(-step/2)
        turtle.right(90)
        turtle.forward(step / 2)
        turtle.left(90)
        turtle.pendown()
        size_square += step

if __name__ == '__main__':
    main()
