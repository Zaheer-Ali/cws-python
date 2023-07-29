"""
Rectangle - Class

inputDimension()
    Ask user - Length, Breadth

area()
    print Area

parameter()
    print parameter


a,b,c
r1,r2,r3
"""


class Rectangle:
    def inputDimension(self):
        self.length = int(input("enter length : "))
        self.breadth = int(input("enter breadth : "))

    def area(self):
        print(self.length*self.breadth)

    def perimeter(self):
        print(2*(self.length+self.breadth))


a = Rectangle()
a.inputDimension()
a.area()
a.perimeter()
