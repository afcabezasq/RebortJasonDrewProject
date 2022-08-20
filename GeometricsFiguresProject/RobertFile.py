class Pentagon:
    def __init__(self, my_dimensions):
        self.sidelength = my_dimensions

    def perimeter(self):
        myside_split = self.sidelength.split(",")
        myside = myside_split[1]
        return 5*(float(myside))