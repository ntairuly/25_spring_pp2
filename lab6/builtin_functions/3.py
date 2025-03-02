a=input()
al=list()
for i in a:
    al.append(i)
al.reverse()
a1=""
for i in al:
    a1+=i
print(a1)
if a.isdigit() and a==a1:
    print("It is palindrome")
else:
    print("It is not palindrome")