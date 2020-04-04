import queue
N = int(input())

q =  queue.Queue()
for i in range(1,10):
    q.put(i)

i = 0
while True:
    out = q.get()
    i += 1
    if i == N:
        break
    b = out*10
    if out%10 > 0:
        q.put(b+out%10-1)
    q.put(b+out%10)
    if out%10 < 9:
        q.put(b+out%10+1)
    
print(out)