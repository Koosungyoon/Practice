#라이브러리로 하면 될듯

N=int(input())
arr=[]

for i in range(N):
    input_data=input().split()
    arr.append((input_data[0],int(input_data[1])))
arr=sorted(arr,key= lambda student:student[1])

for i in arr:
    print(i[0],end=' ')