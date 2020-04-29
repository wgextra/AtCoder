S = str(input())
n = len(S)

if n <= 4:
    print(0)
else:
    l = 0
    r = 4
    rem_div_3 = int(S[l:r+1]) % 3
    cnt = 0

    while True:
        if rem_div_3 == 0:
            num = int(S[l:r+1])
            if num % 673 == 0:
                cnt += 1
        if r == n - 1:
            if r - l == 4: 
                break
            else:
                l += 1
                r = l + 4
                rem_div_3 = int(S[l:r+1]) % 3
        else:
            rem_div_3 = (rem_div_3 + int(S[r+1])) % 3
            r += 1
    print(cnt)