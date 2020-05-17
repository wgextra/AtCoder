import itertools
N,M,X = map(int,input().split())
costs = []
books = []
for _ in range(N):
    entry = list(map(int,input().split()))
    costs.append(entry[0])
    books.append(entry[1:])
    
mxcost = sum(costs) + 1
lst = [list(i) for i in itertools.product([0, 1], repeat=N)]
for item in lst:
    cost = sum([item[0]*item[1] for item in zip(costs,item)])
    Xs = [0] * M
    for i in range(N):
        if item[i] == 1:
            for j in range(M):
                Xs[j] += books[i][j]
    if min(Xs) >= X:
        mxcost = min(mxcost,cost)

if mxcost == sum(costs) + 1:
    print(-1)
else:
    print(mxcost)
    