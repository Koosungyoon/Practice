n,k=map(int,input().split())
cnt=0

while n>=k:
    n2=n%k
    cnt+=n2
    #n을 n의k 정수 나눗셈한 결과
    n=n//k
    cnt+=1

while n>1:
    n-=1
    cnt+=1

print(cnt)


n,k=map(int,input().split())
result=0

while True:
    #(n이 k로 나누어 떨어지는 수가 될 떄까지 1씩 뺴기)
    target=(n//k)*k #이 구문에서 n이 k로 나누어 떨어지는 숫잘르 찾은것!
    result+=n-target
    n=target

    if n<k:
        break
    result+=1
    n//=k

result+=(n-1)
print(result)