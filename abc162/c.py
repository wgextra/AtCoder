def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
N = int(input())

out = 0
gcds = {}
for i in range(1,N+1):
    for j in range(i,N+1):
        for k in range(j,N+1):   
            gcd_num = gcd(gcd(i,j),k)
            if i == j and j == k:
                out += gcd_num
            elif i == j or j == k:
                out += 3 * gcd_num
            else:
                out += 6 * gcd_num
print(out)
