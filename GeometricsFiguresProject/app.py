from figure1 import Circle

def getFiguresPerimeter(name_figure, dimensions):

    if name_figure == "Circle":
        circle = Circle(dimensions)
        return circle.perimeter()


if __name__ == "__main__":
    getFiguresPerimeter()