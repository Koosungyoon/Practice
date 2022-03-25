#입력 -> N(자연수) 1000이하의 자연수
#출력 -> N보다 작은 한수의 개수 출력
'''
import sys

N=int(sys.stdin.readline().strip())
cnt=0
for i in range(N+1):
    #100미만은  모두 한수
    if i<100:
        cnt=i
    #세자리수는 그 숫자(100의자리수-10의자리수)==(10의자리수-1의자리수)
    else:
        a=i//(100)        #100의자리수
        b=(i-(a*100))//10 #10의자리수
        c=i%10            #1의자리수
        if((a-b)==(b-c)):
            cnt+=1
print(cnt)
'''
import sys

#def함수를 생성
def hansu(n):
    cnt=0
    for i in range(n+1):
        n_list=list(map(int,str(i)))#★각 숫자를 쪼개서 각각의 리스트요소로 변환
        if i<100:
            cnt=i
        elif n_list[0]-n_list[1]==n_list[1]-n_list[2]:
            cnt+=1
    return cnt
num = int(sys.stdin.readline().strip())
print(hansu(num))

        