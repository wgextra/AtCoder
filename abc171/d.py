N = int(input())
As = list(map(int,input().split()))
Q = int(input())

lst = [0] * (10**5+1)
for A in As:
    lst[A] += 1

val = sum(As)

vals = []
for i in range(Q):
    B, C = map(int,input().split())
    val += (C-B) * lst[B]
    lst[C] += lst[B]
    lst[B] = 0
    vals.append(val)
for val in vals:
    print(val)