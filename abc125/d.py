input()
ms = list(map(int,input().split()))
ms_abs = [abs(m) for m in ms]
ms_minus = [m for m in ms if m < 0]
if len(ms_minus) % 2 == 0:
    print(sum(ms_abs))
else:
    print(sum(ms_abs) - 2*min(ms_abs))