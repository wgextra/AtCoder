def gcd(u, v):
    if u == v:
        return u
    elif u == 0:
        return v
    elif v == 0:
        return u
    # u is even
    elif u & 1 == 0:
        # v is even
        if v & 1 == 0:
            return 2*gcd(u >> 1, v >> 1)
        # v is odd
        else:
            return gcd(u >> 1, v)
    # u is odd
    elif u & 1 != 0:
        # v is even
        if v & 1 == 0:
            return gcd(u, v >> 1)
        # v is odd and u is greater than v
        elif u > v and v & 1 != 0:
            return gcd((u-v) >> 1, v)
        # v is odd and u is smaller than v
        else:
            return gcd((v-u) >> 1, u)

N = int(input())
As = list(map(int,input().split()))

out = ""
num = 1
for i in range(N-1):
    if out != "not coprime" and gcd(As[i],As[i+1]) == 1:
        out = "pairwise coprime"
    elif gcd(num, As[i+1]) == 1 and i+1 == N:
        out = "setwise coprime"
    else:
        out = "not coprime"
    num = num % As[i]

print(out)



