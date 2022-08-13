# 계수 정렬로 풀면 간단하다. 조건이 1000000이하 이므로 가능함
import sys

input = sys.stdin.readline
n = int(input())
#카운트될 리스트 초기화
data = [0] * 10001
#입력된 수가 있는 위치에 카운트하기
for _ in range(n) :
    data[int(input())] += 1

for i in range(10001) :
    #data에 없는 수면 뛰어넘기 
    if data[i] != 0 :
        for j in range(data[i]) :
            print(i)