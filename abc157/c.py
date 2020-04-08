n,m= map(int,input().split())
inputs = []
for _ in range(m):
    inputs.append(list(map(int,input().split())))

if m == 0:
    if n == 1:
        print(0)
    else:
        print(10**(n-1))
    exit()
elif n == 1:
    if len([i[1] for i in inputs if i[1] != inputs[0][1]]) > 0:
        print(-1)    
    else:
        print(max(0,inputs[0][1]))
    exit()
else:
    out = [-1] * n
    for item in inputs:
        s = item[0]
        c = item[1]
        if out[s-1] != -1 and out[s-1] != c:
            print(-1)
            exit()
        elif s == 1 and c == 0:
            print(-1)
            exit()
        else:
            out[s-1] = c

out[0] = max(out[0],1)
res = 0
for i in range(len(out)):
    if out[i] != -1:
        res += out[i] * 10 ** (n-i-1)
print(res)
        