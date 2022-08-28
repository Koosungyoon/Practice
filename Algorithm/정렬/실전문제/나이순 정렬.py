import sys
n=int(sys.stdin.readline())
data=[]

for _ in range(n):
    #나이와 이름을 입력받음
    input_data=sys.stdin.readline().split()
    #나이는 정수이고 이름은 문자열이므로 다음과 같이 작성
    data.append((int(input_data[0]),input_data[1]))
#나이순으로 정렬 
data=sorted(data,key=lambda a:a[0])

for i in range(n):
    print(data[i][0],data[i][1])
