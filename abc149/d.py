N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

score = 0

last_lst = [""]*K

for i in range(N):
    if T[i] == last_lst[i%K]:
        last_lst[i%K] = ""
        continue
    else:
        if T[i] == "r":
            score += P
        elif T[i] == "p":
            score += S
        else:
            score += R
        last_lst[i%K] = T[i]
print(score)