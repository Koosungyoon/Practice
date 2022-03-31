
#설탕 배달을 하는데 있어서 최소한의 갯수의 봉지를 들고 다니고 싶다.
#이 문제는 설탕의 무게를 나타내는 숫자 N이 입력되면 3 킬로그램과 5 킬로그램으로 된 봉지에 나누어 담아서 가장 적은 수의 봉지 개수를 출력하는 문제이다. 설탕을 나눠 담을 때 정확하게 n이 될 수 없는 경우에는 -1을 출력한다.

'''
import sys

N=int(sys.stdin.readline().strip())

P=N//5
Q=N%5
if Q==0:
    print(P)
else:
    if Q==3:
        print(P+Q//3)
    elif Q==2:
        if P>2:
            P-=2
            Q+=10
            print(P+Q//3)
        else:
            print(-1)
    else:
        if P>0:
            P-=1
            Q+=5
            print(P+Q//3)
        else:
            print(-1)
'''
import sys

N=int(sys.stdin.readline().strip())

bag=0

while(N>=0):
    if N%5==0:
        bag+=N//5
        print(bag)
        break
    else:
        N-=3
        bag+=1
else:
    print(-1)
    '''
    배운점:
    설탕의 봉지 개수를 찾는 코드는 while 반복문을 활용! 5의 배수가 될 때까지 설탕의 무게에서 3씩 빼가는 방식으로 코드를 작성함
    딱 나누어 떨어지지 않을 때는 while - else문을 활용해서 -1을 출력하도록 문제를 풀었다. 
 '''