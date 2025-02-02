def filter_prime(number):
    flag = True
    if number <1:
        flag=False
    for i in range(2,number):
        if number%i==0:
            flag=False
    return flag
isprime = lambda numbers: list(filter(filter_prime,numbers))
print(isprime([1,2,3,4,5,6,7,8,9,10,12,13,17]))