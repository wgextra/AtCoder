def mod_power(x,y,p):
    print(x,y,p)
    if y == 1:
        return x % p
    elif y % 2 == 0:
        return (mod_power(x,y/2,p)**2) % p
    else:
        return (mod_power(x,y-1,p) * x ) % p