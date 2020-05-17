fl = open("sub1_21.txt","r")  #expect 60214

# N,K = map(int,fl.readline().split())
# l = list(map(int,fl.readline().split()))

# seen = set()
# seenl = []
# temp = 1
# for i in range(N):
#     if temp in seen:
#         break
#     else:
#         seen.add(temp)
#         seenl.append(temp)
#         temp = l[temp-1]
# lenloop = len(seenl) - seenl.index(temp) - 1
# loop_pos = (K - i - 1)%lenloop
# before_pos = seenl.index(temp)
# print(seenl[before_pos:][lenloop])

n,k = map(int,fl.readline().split())
l = list(map(int,fl.readline().split()))
seenl = [1]
seen = {1}
temp=1
for i in range(k):
  temp=l[temp-1]
  if temp in seen:
    lenloop = len(seenl)-seenl.index(temp)
    r = (k-i-1)%lenloop
    temp = seenl[seenl.index(temp):][r]
    print(lenloop)
    print(r)
    print(temp)
    break
  seenl.append(temp)
  seen.add(temp)
print(temp)