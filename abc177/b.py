S = input()
T = input()

def count_common(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    return cnt

cnt = 0

for i in range(len(S) - len(T) + 1):
    cnt = max(cnt, count_common(S[i:i+len(T)],T))

print(len(T)-cnt)