class Shape:
    def area(self,area_of_shape=0):
        print(f"The area of the shape is {area_of_shape}")
class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Length:"))
        self.width = int(input("Width:"))
        self.area_of_shape=0
    def area(self):
        self.area_of_shape = self.length*self.width
        super().area(self.area_of_shape)
a=Rectangle()
a.area()