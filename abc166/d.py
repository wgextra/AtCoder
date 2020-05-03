X = int(input())
for B in range(131):
    for A in range(B,131):
        if A**5 - B**5 == X:
            print(str(A) + " " + str(B))
            exit()
        elif A**5 + B**5 == X:
            print(str(A) + " " + str(-1*B))
            exit()