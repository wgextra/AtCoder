N,K = map(int,input().split())

a = N%K
if a == 0:
        print(0)
else:
        if a < K/2:
                print(a)
        else:
                print(K-a)
