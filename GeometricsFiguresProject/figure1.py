class Circle:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.validate_input()
        self.r = self.dimensions.split("r")[1]
        self.p = self.perimeter() #attributes
        self.a = self.area()

    def perimeter(self):   #methods
        p = self.r# "r16" ['','16'], split("1") -> ["r","6"]
        return 2*(3.1416)*int(p)

    def area(self):
        a = (float(self.r)**2)*3.1416
        return a

    def validate_input(self):
        array = self.dimensions.split("r")

        if(len(array) > 2):
            raise Exception("Not valid input")


    def division(self,number1, number2):
        try:
            return number1/number2
        except ZeroDivisionError as e:
            print(str(e) + " Number2 has a wrong value please enter a valid one")