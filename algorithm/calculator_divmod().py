#공통 코드

import sys

input_price = input('투입 금액: ')
if(not input_price.isdecimal() and input_price < 0):
    print('투입 금액에 오류 발생')
    sys.exit()
product_price = input('물건 금액: ')
if(not product_price.isdecimal() and product_price < 0):
    print('물건 금액의 오류 발생')
    sys.exit()

change = int(input_price) - int(product_price)
print('change: '+ str(change))
if(change < 0):
    print('결제할 금액이 부족합니다.')

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

#기존 코드
# for i in coin:
#     p = change // i
#     change = change % i
#     print(str(i)+ ': '+ str(p))


#divmod함수 이용하여 수정한 코드
for i in coin:
    p, change = divmod(change, i)
    print(str(i) + ': '+ str(p))