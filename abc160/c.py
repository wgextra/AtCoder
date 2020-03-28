K,N = map(int,input().split())
As = list(map(int,input().split()))

two_loops = As + [A+K for A in As]

max_dist = 0
max_dist_index = 0
for i in range(len(two_loops)-1):
    new_dist = two_loops[i+1]-two_loops[i]
    if new_dist > max_dist:
        max_dist = new_dist
        max_dist_index = i+1
print(two_loops[max_dist_index+N-1]-two_loops[max_dist_index])