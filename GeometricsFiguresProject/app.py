from figure1 import Circle
from RobertFile import Pentagon

def getFiguresPerimeter(name_figure, dimensions):

    if name_figure == "Circle": #  r15

        circle = Circle(dimensions)
        return circle.perimeter()
    elif name_figure == "Pentagon":
        pentagon = Pentagon(dimensions)
        return pentagon.perimeter()

if __name__ == "__main__":
    print(getFiguresPerimeter("Circle", "r16"))
    print(getFiguresPerimeter("Pentagon", "s,15.3"))
