import functools
n = input()
As = list(map(int,input().split()))
out = 1
for A in As:
    out = out * A
    if out > 10**18:
        break
if out > 10**18:
    print(-1)
else:
    print(out)