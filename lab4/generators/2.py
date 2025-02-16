def even(n):
    for i in range(0,n+1):
        if i % 2 == 0:
            yield str(i)
            if i!=n and i!=n-1:
                yield ","
a = even(int(input()))
b=""
for i in a:
    b+=i
print(b)