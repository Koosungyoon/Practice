#크로아티아 알파벳이 문자열로 주어짐 (소문자와 =,-로 이루어짐)
#주의 할 것은 dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
#위 목록에 없는 알파벳은 한 글자씩 센다
#크로아티아 알파벳 몇글자인지 출력 


import sys

S=sys.stdin.readline().strip()
cro_alp =["c=","c-","dz=","d-","lj","nj","s=","z="]

for cro in cro_alp:
    if cro in S: #예외 발생 -> ddz=z=이런 문자는 중복해서 셀 수있다.
        S=S.replace(cro,"/")
        
print(len(S))


#얻은것 : replace함수를 배움 