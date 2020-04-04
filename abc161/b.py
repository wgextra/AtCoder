N,M = map(int,input().split())
As = list(map(int,input().split()))
As.sort(reverse=True)

if As[M-1] >= sum(As)/(4*M):
    print("Yes")
else:
    print("No")