from collections import Counter 
N = int(input())
Ds = list(map(int,input().split()))
M = int(input())
Ts = list(map(int,input().split()))

d = Counter(Ds)

for t in Ts:
    if d[t] >= 1:
        d[t] = d[t]-1
    else:
        print("NO")
        exit()

print("YES") 

# リストの再構築が遅いからTLE
# Ds.sort()
# Ts.sort()

# def func(Ds,Ts,a):
#     a = a + 1
#     print(a)
#     if Ts == []:
#         return "YES"
#     elif Ds[0] == Ts[0]:
#         return func(Ds[1:],Ts[1:],a)
#     elif Ds[0] < Ts[0]:
#         return func(Ds[1:],Ts,a)
#     else:
#         return "NO"

# print(func(Ds,Ts,1))

