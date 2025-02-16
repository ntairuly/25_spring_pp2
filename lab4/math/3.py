import math
def area_polygon():
    sides = int(input("Input number of sides: "))
    length = int(input("Input the length of a side: "))
    area = int((sides*math.pow(length,2))/(4*math.tan(math.pi/sides)))
    print(f"The area of the polygon is: {area}")
area_polygon()