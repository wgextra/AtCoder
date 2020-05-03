import math
X = int(input())
p = 100
i = 0
while True:
    i += 1
    p = math.floor(p*1.01)
    if p >= X:
        break
print(i)