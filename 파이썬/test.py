import sys
#소수는 2를 제외하고 홀수이므로 2와 홀수 전체 집합에서 홀수의 배수를 제거 하는방법!
nums={x for x in range(2,10001) if x==2 or x%2==1}
for odd in range(3,101,2): #100=sqrt(10000)
    nums-={i for i in range(2*odd,10001,odd) if i in nums}


n=int(sys.stdin.readline().strip())
for i in range(n):
    a=int(sys.stdin.readline().strip())
    b=a//2
    for x in range(b,1,-1):
        if (a-x)in nums and x in nums:
            print(x,a-x)
            break
