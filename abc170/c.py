x,n = map(int,input().split())
ps = list(map(int,input().split()))
ps.sort()

allowed = []
for i in range(102):
    if i not in ps:
        allowed.append(i)

for j in range(len(allowed)-1):
    if x-allowed[j+1] == 0:
        print(x)
        exit()
    elif (x-allowed[j]) * (x-allowed[j+1]) > 0:
        continue
    else:
        if x-allowed[j] <= allowed[j+1] - x:
            print(allowed[j])
        else:
            print(allowed[j+1])