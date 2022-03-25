#입력 -> 알파벳소문자로 이루어진 단어S
#출력 -> 알파벳의 처음등장하는 위치 + 알파벳 순서대로 출력됨
'''
import sys

S=sys.stdin.readline().strip()
#list생성->AtoZ
alp=[]
for i in range(28):
    alp.append(-1)
for j in S:
    alp[ord(j)-97]=S.find(j)

for k in alp:
    print(k)
'''
import sys

S=sys.stdin.readline().strip()
#alp = list(range(97,123)) #아스키 숫자 범위(a-z)

for i in range(97,123):
    print(S.find(chr(i)))
#얻은 것: find 함수
#결론 : S를 탐색하는 것이 아니라 어차피 출력은 알파벳 순서대로이므로 a부터 z까지 순서대로 S를 탐색하며 알파벳이 존재하는 위치를 출력해주면 된다.  