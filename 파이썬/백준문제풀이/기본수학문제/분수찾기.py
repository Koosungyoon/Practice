#N번째분수를 찾기!
import sys

N=int(sys.stdin.readline().strip())

line=0 #사선이 짝수인지 홀수 인지 판별하려고!
k=0 #분수들의 갯수합!
while (N>k):
    line+=1
    k+=line

gap=k-N
if line%2==0:
    up=line-gap
    down=1+gap
else:
    up=1+gap
    down=line-gap
print("%d/%d"%(up,down))
