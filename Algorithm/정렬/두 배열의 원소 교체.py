#선택 정렬을 이용 해볼까?
#각각을 정렬하고 작은 수하고 큰수하고 바꾸면 될 듯한디...
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    a[i],b[i]=b[i],a[i]

print(sum(a))

#간과한 점: 배열 a의 작은수가 배열b의 큰 수보다 클 수도 있다는 점...

n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break
print(sum(a))