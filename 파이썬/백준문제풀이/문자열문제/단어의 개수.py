#입력 -> 영어 대소문자와 공백으로 이루어진 문자열 
#       단어는 공백 한 개로 구분됨 또한 문자열은 공백으로 시작 하거나 끝날 수 있다!
#출력 -> 단어의 개수를 출력하시오 len(s_list)로 출력할 것

import sys

S=sys.stdin.readline().strip()
S_list = list(S.split())

print(len(S_list))

