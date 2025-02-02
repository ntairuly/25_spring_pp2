def spy_game(nums):
    n=0
    for i in nums:
        if i == 0:
            n+=1
        elif i == 7:
            if n>=2:
                print(True)
                return True
            n=0
    print(False)
    return False        

spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])