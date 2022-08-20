from figure1 import Circle
from RobertFile import Pentagon

def getFiguresPerimeter(name_figure, dimensions):

    if name_figure == "Circle": #  r15
        try:
            circle = Circle(dimensions)
            return circle.perimeter()
        except Exception as e:
            print(e)

    elif name_figure == "Pentagon":
        pentagon = Pentagon(dimensions)
        return pentagon.perimeter()

if __name__ == "__main__":
    print(getFiguresPerimeter("Circle", "r16"))
    print(getFiguresPerimeter("Circle", "r12r12"))
    c = Circle("r16")
    c.division(1,0)
    print(getFiguresPerimeter("Pentagon", "s,15.3"))
