#그 다음 방으로 가는데 6개씩 방이 늘어난다.and
# 입력 -> 방의 번호를 입력
# 출력 -> 입력된 방까지 최소 몇개를 지나야하는 지 출력 

import sys

N=int(sys.stdin.readline().strip())
#N을 넘으면 끝
k=1 #벌집의 개수, 1부터 시작!
i=1
while (N>k):
    k+=i*6
    i+=1
print(i)

#조금만 더 생각해보면 되는데 너무 아쉽다!
