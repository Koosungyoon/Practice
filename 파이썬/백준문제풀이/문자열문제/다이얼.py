#입력 -> 할머니가 외운 영어 문자열로 입력
#출력 -> 전화거는데 걸리는 시간 

#각각의 알파벳을 문자열과 비교하여 시간확인하기!
'''
import sys
#             2     3     4     5      6     7     8     9
#             3초   4초  5초    6초   7초    8초    9초   10초
alp_list = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S=sys.stdin.readline().strip()
time=0

for alp in alp_list:
    for i in alp:
        for j in S:
            if i==j:
                time += alp_list.index(alp)+3

print(time)         
'''
#아래는 문자열의 문자순서대로 비교한것!
import sys

alp_list =["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S=sys.stdin.readline().strip()
time=0

for i in S:
    for alp in alp_list:
        #S안에 있는 문자가 alp에 있다면 time애 시간추가!
        if i in alp:
            time+=alp_list.index(alp)+3

print(time)