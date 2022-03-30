#내가 구현해야 할 것!-> k층의n-1수의 사람수+ k-1층의n호수 사는 사람수합
'''
4층	1	6	21	56	126
3층	1	5	15	35	70
2층	1	4	10	20	35
1층	1	3	6	10	15
0층	1	2	3	4	5
'''
import sys

T=int(sys.stdin.readline().strip())

for z in range(T):
    #층과 호수 입력
    K=int(sys.stdin.readline().strip())
    N=int(sys.stdin.readline().strip())
    #호수 리스트 
    h_list=list(range(1,N+1))
    #k층의n-1수의 사람수+ k-1층의n호수 사는 사람수합
    #★★★★★★★★★★★★★★★★★★★★★★★★
    for i in range(K):
        for j in range(1,N):
            h_list[j]+=h_list[j-1]
    #★★★★★★★★★★★★★★★★★★★★★★★★
    print(h_list[-1])