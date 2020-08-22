n = input()
As = list(map(int,input().split()))

prev_A = As[0]
total_step_hight = 0
for i in range(1,len(As)):
    if  As[i-1] > As[i]:
        total_step_hight += As[i-1] - As[i]
        As[i] = As[i] + (As[i-1] - As[i])

print(total_step_hight)
