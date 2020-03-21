n, k = map(int,input().split())
def fun(n,k):
    if n < k:
        return str(n)
    else:
        return fun(n//k,k) + str(n%k)
print(len(fun(n,k)))