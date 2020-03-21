import math
n,a,b = map(int,input().split())
n_fact = math.factorial(n)
print(int((2**n-n_fact/math.factorial(a)/math.factorial(n-a)-n_fact/math.factorial(b)/math.factorial(n-b)-1)%(10**9+7)))