N,K = map(int,input().split())
Hs = list(map(int,input().split()))
outs = [1] * N
for _ in range(K):
    a,b = map(int,input().split())
    if Hs[a-1] == Hs[b-1]:
        outs[a-1] = 0 
        outs[b-1] = 0 
    elif Hs[a-1] > Hs[b-1]:
        outs[b-1] = 0 
    else:
        outs[a-1] = 0 
print(sum(outs))