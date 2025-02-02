def has_33(nums):
    n=0
    for i in nums:
        if i==3:
            n+=1
            if n==2:
                print(True)
                return True
        else:
            n=0
    print(False)
    return False

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3]) 