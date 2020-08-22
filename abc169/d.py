N, M = map(int,input().split())

room = {}
startRoom = {1:1}

for i in range(M):
  A, B = map(int,input().split())
  room.setdefault(A, []).append(B)
  room.setdefault(B, []).append(A)
  
targetRoom = [1]
while len(targetRoom) != 0:
  nextTarget = []
  for i in targetRoom:
    roomList = room[i]
    for j in roomList:
      if j not in startRoom:
        startRoom[j] = i
        nextTarget.append(j)
  targetRoom = nextTarget
  
if len(startRoom) != N:
  print("No")
else:
  print("Yes")
  for i in range(2, N+1):
    print(startRoom[i])
