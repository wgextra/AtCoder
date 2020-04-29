def mod_power(x,y,p):
    if y == 1:
        return x % p
    elif y % 2 == 0:
        return (mod_power(x,y/2,p)**2) % p
    else:
        return (mod_power(x,y-1,p) * x ) % p

def mod_inv(x,p):
    return mod_power(x,p-2,p)

def mod_nCa(n,a,p):
    num = 1
    den = 1
    for i in range(a):
        num = (num * (n-i)) % p
        den = (den * (a-i)) % p
    return (num * mod_inv(den,p)) % p


n,a,b = map(int,input().split())

m = 10**9 + 7

print((mod_power(2,n,m) - mod_nCa(n,a,m) - mod_nCa(n,b,m) - 1) % m)
