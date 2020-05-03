import math
N,K = map(int,input().split())
has = [0]*(N+1)
for _ in range(K):
    input()
    items = list(map(int,input().split()))
    for item in items:
        has[item] = 1

print(N - sum(has))
        
