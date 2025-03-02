import math
l = list()
num = int(input("How many numbers?\n"))
for i in range(num):
    l.append(int(input()))
print(math.prod(l))