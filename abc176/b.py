n = list(map(int,list(input())))
val = 0
for i in n:
    val += i
if val %9 == 0:
    print("Yes")
else:
    print("No")