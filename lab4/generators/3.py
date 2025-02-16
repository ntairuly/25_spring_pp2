def  div3_4(n):
    for i in range(0,n+1):
        if i % 4 == 0 and i % 3 == 0:
            yield i
a = div3_4(int(input()))
for i in a:
    print(i)