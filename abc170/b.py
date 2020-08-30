x,y = list(map(int,input().split()))
if y > 4*x:
    print("No")
elif y < x*2:
    print("No")
elif y % 2 == 1:
    print("No")
else:
    print("Yes")