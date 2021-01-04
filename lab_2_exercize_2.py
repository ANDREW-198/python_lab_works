import turtle
def main():
    draw_square()

def draw_square(size_square=100):
    turtle.shape('turtle')
    for i in range(4):
        turtle.forward(size_square)
        turtle.left(90)




if __name__ == '__main__':
    main()

