#입력 -> 문자열  (upper함수로 대문자로 바꾸기)
#출력 -> 가장 많이 사용된 알파벳 대문자로 출력 
#        만약에 위의 조건의 알파벳이 2개 이상이면 ?출력

import sys

S=(sys.stdin.readline().strip()).upper()
unique = list(set(S))
alp_list = []
cnt_list=[]
for i in S:
    alp_list.append(i)

for j in unique:
    cnt=S.count(j)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list))>1:
    print("?")
else:
    max_index=cnt_list.index(max(cnt_list))
    print(unique[max_index])


