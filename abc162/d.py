import math
N = int(input())
S = input()

R = len([s for s in S if s == "R"])
G = len([s for s in S if s == "G"])
B = len([s for s in S if s == "B"])

out = R * G * B
for i in range(N):
    intvl = math.ceil((N - i)/2)
    for j in range(1,intvl):
        if S[i] != S[i+j] and S[i+j] != S[i+2*j] and S[i] != S[i+2*j]:
            out -= 1
print(out)