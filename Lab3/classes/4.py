class Point:
    def __init__(self):
        self.x = " "
        self.y = " "
        self.z = " "
        self.x_lenght = " "
        self.y_lenght = " "
        self.z_lenght = " "
    def show(self):
        if type(self.x)==int:
            print(f"Coordinates:\nx:{self.x}\ny:{self.y}\nz:{self.z}")
        else:
            print("Lack of information")
    def move(self):
        print("Move coordinates:")
        self.x = int(input("x:"))
        self.y = int(input("y:"))
        self.z = int(input("z:"))
    def dist(self,self1):
        x_lenght=self.x-self1.x
        y_lenght=self.y-self1.y
        z_lenght=self.z-self1.z
        self.distance=(x_lenght**2 + y_lenght**2 + z_lenght**2)**0.5
        print(f"Distance between two coordinates:{self.distance}")
a=Point()
a.move()
b=Point()
b.move()
a.show()
a.dist(b)