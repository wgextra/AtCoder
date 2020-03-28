X,Y,A,B,C = map(int,input().split())
reds = list(map(int,input().split()))
greens = list(map(int,input().split()))
nos = list(map(int,input().split()))

reds.sort(reverse=True)
greens.sort(reverse=True)
nos.sort(reverse=True)

bests = reds[:X]+greens[:Y]
bests.sort(reverse=True)

very_bests = []

for best in bests:
        if best > nos[0]:
                very_bests.append(best)
        else:
                very_bests.append(nos[0])
                nos = nos[1:]

print(sum(very_bests))