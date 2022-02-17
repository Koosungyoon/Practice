'''
string_a = "{}".format(10)

print(string_a)
print(type(string_a))


output_a = "{:+5d}".format(52) # 기호를 뒤로 민다 
output_b = "{:+5d}".format(-52)
output_c = "{:=+5d}".format(52) # 빈칸과 부호 조합시 사용 (부호가 앞에 온다)
output_d = "{:=+5d}".format(-52)
output_e = "{:05d}".format(52) # 빈칸 0으로 채우기
output_f = "{:05d}".format(-52)

#조합하기
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print(output_f)
'''
name = "{:=+05d}".format(52)

print(name)
