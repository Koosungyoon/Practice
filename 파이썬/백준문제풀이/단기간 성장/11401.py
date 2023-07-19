# 문제 : 이항 계수 구하는 방법! 

# 최종 -> 분할 정복 제곱 기법을 사용함! -> 새로 배운 개념 
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

################################
#DP 사용하여 문제 풀이 -> 메모리 초과
import sys

a = 1000000007

def init(n, K):
    res = [[a for _ in range(n)] for _ in range(K + 1)]
    for i in range(n):
        res[0][i] = 1
        res[1][i] = i + 1
        if i < K:
            res[i + 1][i] = 1
    return res

def DP(N, K, res):
    if res[K][N - 1] == a:
        res[K][N - 1] = DP(N - 1, K - 1, res) + DP(N - 1, K, res)
    return res[K][N - 1]

def calculate_combinations(N, K):
    res = init(N, K)
    result = DP(N, K, res)
    return result

# Read input from command line
N, K = map(int, sys.stdin.readline().strip().split())

result = calculate_combinations(N, K)
print(result % a)






