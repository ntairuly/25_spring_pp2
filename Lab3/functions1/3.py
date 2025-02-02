def solve(numheads, numlegs):
    rabbits = int(numlegs/2 - numheads)
    chickens = int(abs(rabbits - numheads))
    print(f"Chickens:{chickens} \nRabbits:{rabbits}")
numheads, numlegs = 35,94
solve(numheads,numlegs)