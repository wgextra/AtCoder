n = int(input())
As = list(map(int,input().split()))

out = 0
num = 1
for A in As:
    if  A == num:
        num += 1
    else:
        out += 1
if out == n:
    print(-1)
else:
    print(out)
    