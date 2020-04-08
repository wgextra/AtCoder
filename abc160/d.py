n,x,y = map(int,input().split())
dists = [0]*(n)
for i in range(1,n+1):
    for j in range(1,i):
        dists[min(i-j,abs(j-x)+1+abs(i-y))]+=1
    
for i in range(1,len(dists)):
    print(dists[i])