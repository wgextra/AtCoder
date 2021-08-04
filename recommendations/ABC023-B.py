N = int(input()) // 2
S = input()

out = "b"
for i in range(N+1):
    if i == 0:
        continue
    elif i % 3 == 1:
        out = "a" + out + "c"
    elif i % 3 == 2:
        out = "c" + out + "a"
    else:
        out = "b" + out + "b"

if out == S:
    print(N)
else:
    print(-1)