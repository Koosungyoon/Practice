import sys

n=int(sys.stdin.readline().strip())
for i in range(n):
    a=int(sys.stdin.readline().strip())
    b=[False,False]+[True]*(a-1)
    prime=[]
    for j in range(2,a+1):
        if b[j]:
            prime.append(j)
            for k in range(j*2,a+1,j):
                b[k]=False
    c=a-prime[len(prime)//2]
    while(True):
        i=1
        if c in prime:
            if c>(a-c):
                print((a-c),c)
            else:
                print(c,(a-c))
            break
        else:
            c=a-prime[len(prime)//2+i]
            i+=1