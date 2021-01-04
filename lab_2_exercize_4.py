import turtle

def main():
    draw_polygon()


def draw_polygon(number_side=10s0,
                 size_side=10):

    turtle.shape('turtle')
    for i in range(number_side):
        turtle.forward(size_side)
        turtle.left(360/number_side)




if __name__ == '__main__':
    main()