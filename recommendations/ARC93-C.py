# https://atcoder.jp/contests/arc093/tasks/arc093_a
N = int(input())
As = list(map(int,input().split()))

As = [0] + As + [0]

total = 0
for i in range(len(As)-1):
    total = total + abs(As[i] - As[i+1])

for i in range(len(As)-2):
    print(total - abs(As[i] - As[i+1]) - abs(As[i+1] - As[i+2]) + abs(As[i] - As[i+2]))

