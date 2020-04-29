N = int(input())
items = []

for i in range(N):
    item = input()
    items.append(item)    
items.sort()
cnt = 0
before = ""
for index,item in enumerate(items):
    if index == 0:
        cnt += 1    
    elif before != item:
        cnt += 1
    before = item
print(cnt)