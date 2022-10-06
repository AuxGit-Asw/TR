import heapq

def lastStoneWeight(weights):
    for i in range(len(weights)):
        weights[i] *= -1
    heapq.heapify(weights)
    while weights and len(weights) > 1:
        print(weights)
        largest = heapq.heappop(weights)
        seclargest = heapq.heappop(weights)
        
        print(largest, seclargest)
        if largest == seclargest:
            continue
        else:
            largest -= seclargest
            heapq.heappush(weights, largest)
    if not weights:
        return 0
    return -1*weights[0]

print(lastStoneWeight([1,2,3,6,7,7]))