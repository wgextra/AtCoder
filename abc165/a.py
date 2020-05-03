K = int(input())
A, B =  map(int,input().split())
if len([i for i in range(A,B+1) if i % K == 0]) == 0:
    print("NG")
else:
    print("OK")