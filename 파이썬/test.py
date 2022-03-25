#문자열 입력 받고 가장많이 사용된 알파벳 문자 대문자로 출력 하는 프로그램
import sys

S = sys.stdin.readline().strip().upper()

unique=list(set(S)) #알파벳 종류 리스트 -> 알파벳순서대로 입력됨
cnt_list=[]
for i in unique:
    cnt=S.count(i)
    cnt_list.append(cnt)


if cnt_list.count(max(cnt_list))>1:
    print("?")

else:
    max_index=cnt_list.index(max(cnt_list))
    print(unique[max_index])