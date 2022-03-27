#입력 -> 두 수는 갗지 않는 세자리수 0이 포함되어있지 않다 
#        상수는 두 수를 거꾸러 뒤집어 숫자 크기를 비교한다 
#reverse 함수 사용?? 리스트에서 적용됨 -> reversed 함수 이용

import sys

a,b =sys.stdin.readline().strip().split()

re_a=''.join(reversed(a)) #enumerate
re_b=''.join(reversed(b))

if re_a>re_b:
    print(re_a)
else:
    print(re_b)



