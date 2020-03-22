import math
input()
items = list(map(int,input().split()))
for i in range(len(items)):    
    rest = items[:i] + items[i+1:]
    rest_unique = set(rest)
    out = 0
    for j in rest_unique:
        cnt = sum([1 for x in rest if x == j])
        if cnt >= 2:
            out = out + math.factorial(cnt)/math.factorial(cnt-2)/2
    print(int(out))