n = int(input())
m = n%10

if m in [2,4,5,7,9]:
    print("hon")
elif m in [0,1,6,8]:
    print("pon")
else:
    print("bon")
