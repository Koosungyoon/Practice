#0/1 knapsack 문제

import sys
input = sys.stdin

n,k = map(int,input.readline().split())
knapsack = [0 for _ in range(k + 1)]

product = [[0,0]]
for _ in range(1,n+1):
    product.append(list(map(int,input.readline().split())))

for x in range(1,k+1):
    knapsack[x] = 0
    for i in range(1,n+1):
        if product[i][0] <= x:
            knapsack[x] = max(knapsack[x], knapsack[x - product[i][0]] + product[i][1])

print((knapsack))


#Knapsack
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

stuff = [[0,0]]
DP = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = stuff[i]
        if j >= w:
            DP[i][j] = max(DP[i-1][j] , DP[i-1][j-w] + v)
        else:
            DP[i][j] = DP[i-1][j]

print(DP[i])