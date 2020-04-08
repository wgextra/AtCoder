import queue
q = queue.Queue()
N,K = map(int,input().split())
ds = list(map(int,input().split()))

sm = sum(ds[:K])
out = sm
for i in range(N-K):
    sm = sm-ds[i]+ds[i+K]
    out = max(out,sm)

print((out+K)/2)