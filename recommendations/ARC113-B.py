# https://atcoder.jp/contests/arc113/tasks/arc113_b
A,B,C= map(int,input().split())

A = A % 10
B = (B - 1) % 4 + 1
C = (C - 1) % 4 + 1

print((A**(B**C))%10)