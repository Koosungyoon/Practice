#피보나치 함수 소스코드

def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

# 피보나치 수열 소스코드(재귀적)

#한 번 계산된 결과를 메모제이션(memozation)하기 위한 리스트 초기화
d=[0]*100
#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    #종료조건
    if x==1 or x==2:
        return 1
    #이미 계산된 결과하면 그대로 반환
    if d[x]!=0:
        return d[x]
    #아직 계산되지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

#피보나치 수열 소스코드(반복적)

#한 번 계산된 결과를 저장할 DP 테이블 초기화
d=[0]*100
d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
    
