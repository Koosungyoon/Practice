#주사위의 개수에 따라서 나누기(논리 연산자 적용?)
'''
1.3개다 같 -> 10000+(같은눈)*1000 6가지
2.2개만 같 -> 1000+(같은눈)*100
3.모두 다름 -> 가장 큰 수 *100
'''
'''
a,b,c = map(int,input().split()) #주사위 번호 3개 입력
d=0
k=0
if a == b == c:
    d+=10000+a*1000
if a!=b!=c:
    if a>b:
        if b>c:
            k=a
        else:
            if c>a:
                k=c
            else:
                k=a
    else:
        if a>c:
            k=b
        else:
            if c>b:
                k=c
            else:
                k=b
    d+=k*100
else:
    if a==b!=c :
        d+=1000+a*100
    elif b==c!=a:
        d+=1000+b*100
    elif c==a!=b:
        d+=1000+c*100

print(d)
''' #max함수를 깜빡함 !!!!

a,b,c=map(int,input().split())
result =0 
if a==b==c:
    result = 10000+a*1000
elif a==b:
    result =1000+a*100
elif b==c:
    result =1000+b*100
elif c==a:
    result =1000+c*100
else:
    result =100*max(a,b,c)
print(result)    


