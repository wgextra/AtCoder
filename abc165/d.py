import math
A,B,N = map(int,input().split())

if B > N:
    x = N
else:
    x = B - 1
print(int(math.floor(A*x/B)-A*math.floor(x/B)))