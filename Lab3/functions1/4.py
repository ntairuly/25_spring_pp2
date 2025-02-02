def filter_prime(list_of_numbers):
    list_of_prime =[]
    for i in list_of_numbers:
        flag=True
        n=2
        while n<i:
            if(i%n==0):
                flag = False
            n+=1
        if flag:
            list_of_prime.append(i)
    print(list_of_prime)
list_of_numbers = list(input("Enter numbers:").split())
for i in range(len(list_of_numbers)):
    list_of_numbers[i]=int(list_of_numbers[i])
filter_prime(list_of_numbers)                 