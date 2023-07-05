# 10진수를 2진수로 변환하는 프로그램

#변환하고 싶은 10진수 숫자 입력
decimal_number = input('10진수 숫자: ')
if(int(decimal_number) < 0 and not decimal_number.isdecimal()):
    print('올바른 양수를 입력하세요')

#int로 변환
decimal_number = int(decimal_number)

#변환할 진수
to_number = 2

#변환한 값을 담을 문자열
str_number = ''

#변환 작업
while(decimal_number > to_number):
    str_number += str(int(decimal_number % to_number))
    decimal_number /= to_number
    if(decimal_number < to_number): #마지막 나눗셈일 때는 그대로 붙이기
        str_number += str(int(decimal_number))
    
print('2진수: '+ str_number[::-1])