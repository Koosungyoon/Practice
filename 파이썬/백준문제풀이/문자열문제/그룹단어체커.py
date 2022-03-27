#그룹단어 체크 
#같은 알파벳이 떨어져 있으면 그룹단어가 아니다. 
#입력 -> N개의 단어 입력 
#출력 -> 그룹 단어의 개수를 출력 

import sys

N=int(sys.stdin.readline().strip())
cnt=N
a_list=[]
for i  in range (N):
    a_list.append(sys.stdin.readline().strip())
for j in a_list:
    for k in range(len(j)-1): #len(j)라고 하면 범위에러 발생한다.
        #연속하는 문자가 같으면 넘어가기
        if j[k]==j[k+1]:
            pass
        #그렇지 않고 자신의 문자가 나머지문자열에 존재하면 그룹단어가 아니므로 cnt -1 하고 반복문 빠져나오기!
        elif j[k] in j[k+1:]:
            cnt-=1
            break
print(cnt)





