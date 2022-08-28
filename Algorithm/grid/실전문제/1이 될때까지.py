#최대한 많이 나누기 하면 될거 같다.

'''
n,k=map(int,input().split())
cnt=0
#n이 k이상이라면 k로 계속 나누기 
while(n>=k):
    #n이 k로 나누어 떨어질떄 까지 n에 -1 해주기
    while n%k!=0:
        n-=1
        cnt+=1
    #n//k
    n=n//k
    cnt+=1
#마지막으로 남은 수에 대하여 -1해주기
while n>1:
    n-=1
    cnt+=1

print(cnt)
'''
#다시 구현 해보기
'''
n=25 k=3 인경우 
25=3*8+1 =3*(3*2+2)+1 =3*(3*(1+1)+2))+1
k이하인 나머지인 (1과2와1) cnt에 추가되므로 cnt=4이고 k로 나눈 횟수가 2번이므로 cnt=6
'''
n,k=map(int,input().split())
cnt=0

while n>=k:
    n2=n%k
    cnt+=n2
    #n을 n의k 정수 나눗셈한 결과
    n=n//k
    cnt+=1

cnt+=(n-1)
print(cnt)


n,k=map(int,input().split())
result=0

while True:
    #(n이 k로 나누어 떨어지는 수가 될 떄까지 1씩 뺴기)
    target=(n//k)*k #이 구문에서 n이 k로 나누어 떨어지는 숫잘르 찾은것!
    result+=n-target
    n=target
    #n이 k보다 자을떄 반복문 탈출
    if n<k:
        break
    #k로나누기
    result+=1
    n//=k
#마지막으로 남은 수에 대하여 1씩 뺴기
result+=(n-1)
print(result)