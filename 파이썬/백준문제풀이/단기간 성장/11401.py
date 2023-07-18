#DP 문제 풀이인줄 알고 접근하려 했으나 런타임 오류로 -> 분할 정복 제곱 기법을 사용함! -> 새로 배운 개념 
import sys

a = 1000000007

N, K = map(int,sys.stdin.readline().strip().split())

def fact(N):
    n = 1
    for i in range(2,N+1):
        n = (n * i) % a
    return n


def DevideConQuerSquare(C, n):
    if n == 0: return 1
    elif n == 1: return C
    
    tmp = DevideConQuerSquare(C, n // 2)

    if n % 2 == 0: return tmp * tmp  % a
    else: return tmp * tmp * C % a

res = fact(N) * DevideConQuerSquare((fact(N-K) * fact(K)), a-2) % a
print(res)

