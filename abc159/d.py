import math
input()
items = list(map(int,input().split()))
d = {}
for i in items:
    if i in d.keys():
        d[i] = d[i]+1
    else:
        d[i] = 1

p = {}
for k in d.keys():
    cnt = d[k]
    p[k] = (cnt*(cnt-1))/2

total = sum(p.values())

for item in items:
    print(int(total - d[item] + 1))