N,K = map(int,input().split())
val = 0
for i in range(K,N+2):
    mn = i*(i-1)/2
    mx = (2*N-i+1)*i/2
    val += mx - mn + 1
print(int(val)%(10**9 + 7))