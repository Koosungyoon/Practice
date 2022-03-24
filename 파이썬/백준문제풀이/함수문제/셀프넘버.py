'''
#우선 d(n)이라는 함수를 구현
def d(n):
    res=n+n//10+n%10    
    return res

#1~10000까지 반복문을 통해 리스트 구현
a=[]
for i in range(10000):
    a.append(i)

for k in range(10000):
    if d(k)<10000:    
        a.remove(d(k))
    else:
        continue
    
print(a)
'''
'''
#뭔가 리스트에서 제외시키는 방법을 해보려 했지만 출력된 값이 잘못됨을 느낌
#또한 3자리수 이상부터는 d(n)함수가 잘못 구현됨
#그래서 set라는  자료형을 사용해보려함 -> set끼리는 뺴기 가능

a=set(range(1,10001))
rmv=set()

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    rmv.add(i)
a-=rmv
for k in sorted(a):
    print(k)
'''
#for문과 문자열을 활용하여 함수구현
def d(n):
    for i in str(n):
        n+=int(i)
    return n

#1~10000까지 반복문을 통해 리스트 구현
a=[]
for i in range(10001):
    a.append(i)

for j in range(10001):
    if d(j) in a:
        a.remove(d(j))
    
print(a)