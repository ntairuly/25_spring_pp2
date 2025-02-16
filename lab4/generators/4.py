def squares(a,b):
    for i in range(a,b+1):
        yield i**2
a = squares(int(input()),int(input()))
for i in a:
    print(i) 