def getMinimumOperations(items):
    firstOdd = 0
    firstEven = 0
    
    for i in range(len(items)):
        if i % 2 == 0:
            if items[i] % 2 == 0:
                firstOdd += 1
            else:
                firstEven += 1
        