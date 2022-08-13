class Circle:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def perimeter(self):
        p = self.dimensions.split("r")# "r16" ['','16'], split("1") -> ["r","6"]
        p = p[1]
        return 2*(3.1416)*int(p)