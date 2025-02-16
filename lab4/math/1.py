import math
def rad():
    degree = int(input("Input degree: "))
    radian = round(((degree * math.pi)/180),6)
    print(f'Output radian: {radian}')
rad()