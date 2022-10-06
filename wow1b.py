def magicstick(input1, input2, input3):
    mincost = -1
    for i in range(input1):
        currcost = 0
        for j in range(input1):
            currcost += abs(input2[i] - input2[j])*input3[j]
        
        if mincost == -1:
            mincost = currcost
        else:
            mincost = min(mincost, currcost)
            
    return mincost


input1 = 3
input2 = [1, 2, 3]
input3 = [500, 30, 40]

print(magicstick(input1, input2, input3))