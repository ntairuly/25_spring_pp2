word = input("Word:")
up=0
low=0
for i in word:
    if i.isupper():
        up+=1 
    elif i.islower():
        low+=1    
print("Upper case letters:",up)
print("Lower case letters:",low)
