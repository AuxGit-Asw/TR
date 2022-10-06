url = input()
n = int(input())
params = list(input().split())
pvals = list(map(int, input().strip().split()))

valid_values = {}
for i in range(n):
    valid_values[params[i]] = pvals[i]
    
status_good = True

base, parameters = url.split('?')
parameters = parameters.split(',')

paramdict = {}
for parameter in parameters:
    key, value = parameter.split("=")
    value = int(value)
    paramdict[key] = value
    
    if value > valid_values[key]:
        status_good = False
    
paramdict = sorted(paramdict.items())

print(base)
print(len(paramdict))
for k, v in paramdict:
    print(f'{k} {v}')
if status_good:
    print("200")
else:
    print("404")