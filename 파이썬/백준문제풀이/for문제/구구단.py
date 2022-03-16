#N을 입력 -> N구구단 출력

a= int(input())
for i in range(9):
    print("%d * %d = %d"%(a,i+1,a*(i+1)))