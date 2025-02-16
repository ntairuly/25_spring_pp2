def down_to_0(n):
    for i in range(n,-1,-1):
        yield i
a = down_to_0(int(input()))
for i in a:
    print(i) 