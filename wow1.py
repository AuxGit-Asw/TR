def magicstick(input1, input2, input3):
    data = []
    for i in range(input1):
        data.append([input2[i], input3[i], input2[i]*input3[i]])
    
    data = sorted(data, key=lambda x : x[1])
    data = sorted(data, key=lambda x : x[0])
    data = sorted(data, key=lambda x : x[2])
    
    print(data)
    
    center = 0
    if input1 % 2 == 0:
        center = data[input1 // 2][0]
    else:
        center = data[(input1 - 1) // 2][0]
        
    ans = 0
        
    for pair in data:
        ans += (abs(pair[0] - center)*pair[1])
        
    return ans

input1 = 3
input2 = [1, 2, 3]
input3 = [500, 30, 40]

print(magicstick(input1, input2, input3))