import sys
x_num=[]
y_num=[]
for i in range(3):
    x,y=map(int,sys.stdin.readline().strip().split())
    x_num.appned(x)
    y_num.append(y)
for j in x:
    if x_num.count(j)==1:
        a=j 
for k in y:
    if y_num.count(k)==1:
        b=k
print(a,b)    