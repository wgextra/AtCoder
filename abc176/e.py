from collections import deque

h,w,m = map(int,input().split())
Ms = []

h_scores = [0 for i in range(h)]
w_scores = [0 for i in range(w)]

record = list()

for i in range(m):
  h,w = map(int,input().split())
  record.add((h-1,w-1))
  h_scores[h-1] += 1
  w_scores[w-1] += 1

max_h = max(h_scores)
max_w = max(w_scores)
max_h_poss = [i for i,v in enumerate(h_scores) if v == max_h]
max_w_poss = [i for i,v in enumerate(w_scores) if v == max_w]

out_pos_count = 0 

c = False

for i in max_h_poss:
    for j in max_w_poss:
        if (i,j) not in record:
            c = True
            break        

if c:
    print(max(h_scores) + max(w_scores))
else:
    print(max(h_scores) + max(w_scores)-1)