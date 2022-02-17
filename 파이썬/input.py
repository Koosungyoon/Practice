'''
number = input("숫자를 입력하시오>")
print(type(number))

# 문자열을 숫자로 바꾸기(str --> int)

number1 = int(input("숫자를 입력하시오2>"))
print(type(number1))
'''
# swap 하는 방법

a = input("문자열 입력>")
b = input("문자열 입력>")

c = a
a = b
b = c

print(a,b)

#튜플을 이용하여 swap
a,b = b,a
print(a,b)