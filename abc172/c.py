n,m,k = map(int,input().split())
As = list(map(int,input().split()))
Bs = list(map(int,input().split()))


memo = {}
def fun(As,Bs,time_rem):
    if time_rem < 0:
        return -1
    if As == [] and Bs == []:
        return 0
    elif As == []:
        out = fun([],Bs[1:],time_rem-Bs[0])
        if ([],Bs[1:],time_rem-Bs[0]) in memo.keys():
            out = memo[([],Bs[1:],time_rem-Bs[0])]
        else: 
            memo[([],Bs[1:],time_rem-Bs[0]]] = 1 + fun([],Bs[1:],time_rem-Bs[0])
        return out
    elif Bs == []:
        return 1 + fun(As[1:],[],time_rem-As[0])
    else:
        return 1 + max(fun(As[1:],Bs,time_rem-As[0]),fun(As,Bs[1:],time_rem-Bs[0]))

print(fun(As,Bs,k))
