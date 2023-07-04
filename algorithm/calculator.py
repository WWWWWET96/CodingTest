#최소 화폐 개수로 거스름돈을 반환하는 프로그램

import sys

#투입 금액, 상품 금액 입력
input_price = input('input ')
if not input_price.isdecimal or (int(input_price)  0)
    print('양수를 입력하세요.')
    sys.exit() # 에러가 발생하면 강제종료


product_price = input('product ')
if not product_price.isdecimal or (int(product_price)  0)
    print('양수를 입력하세요')
    sys.exit() # 에러가 발생하면 강제 종료

#거스름 돈 계산
change = int(input_price) - int(product_price)
#에러 체크
if change  0
    print('금액이 부족합니다')
    sys.exit()

print('거스름돈',change)


#코인 배열
coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

#계산
for i in coin
    r = change  i
    change = change % i
    print(str(i),' ',str(r))