import math
e,o = map(int,input().split())
if e < 2:
    e_cases = 0
else:
    e_cases = math.factorial(e)/math.factorial(e-2)/2
if o < 2:
    o_cases = 0
else:
    o_cases = math.factorial(o)/math.factorial(o-2)/2
print(int(e_cases+o_cases))