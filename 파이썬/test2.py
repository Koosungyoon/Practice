#n은 n제곱근이하의 소수로 나누어 떨어지지 않으면 소수이다! 구현 
prime =[2,3]+[None]*498
ptr=2

for n in range(5,1001,2): #4이상의 짝수는 제외
    i=1
    while prime[i]**2<=n: #n제곱근이하의 수이면 실행한다!
        if n%prime[i]==0:
            break
        i+=1
    else:
        prime[ptr]=n
        ptr+=1
    
print(prime)