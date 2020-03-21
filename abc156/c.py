input()
xs = list(map(int,input().split()))
x_min = min(xs)
x_max = max(xs)
diss = []
for p in range(x_min,x_max+1):
    diss.append(sum([(p-x)**2 for x in xs]))
print(min(diss))
