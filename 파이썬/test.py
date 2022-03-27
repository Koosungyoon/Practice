import sys

S=sys.stdin.readline().strip()
cro_alp =["c=","c-","dz=","d-","lj","nj","s=","z="]

for cro in cro_alp:
    if cro in S: #예외 발생 -> ddz=z=이런 문자는 중복해서 셀 수있다.
        S.replace(str(cro),"/")
        print(S)    
