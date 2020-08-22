n,k = map(int,input().split())
ps = list(map(int,input().split()))
ps.sort()
print(sum(ps[:k]))