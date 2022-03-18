#입력 -> 몇번 할 것인가(N) N번 동안 숫자 두개 입력 해줄 것
#리스트에 결과값 저장하고 반복문 이용해서 출력
N = int(input())
list=[]
for i in range(N):
    a,b =map(int,input().split())
    list.append(a+b)
for j in range(N):
    print(list[j]) 