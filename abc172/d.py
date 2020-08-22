# N = int(input())
# As = list(map(int,input().split()))
# Q = int(input())

def seachPrimeNum(N):
    max = int(N**0.5)
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum


print(seachPrimeNum(10**7))