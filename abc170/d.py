N = int(input())
As = list(map(int,input().split()))

As.sort(reverse=True)
As = [A for A in As if As.count(A) == 1]

# cnt = len(As)
# for i in range(len(As)-1):
#   for j in range(i+1,len(As)):
#     if As[i] % As[j] == 0:
#       cnt -= 1
#       break

# print(cnt)
  