import math
def area_trap():
    height = int(input("Height: "))
    base1 = int(input("Base, first value: "))
    base2 = int(input("Base, second value: "))
    area = height*(base1+base2)/2
    print(f"Expected Output: {area}")
area_trap()