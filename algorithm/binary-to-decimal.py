#변환할 2진수
n = '10010'

sum = 0

for i in range(len(n)):
    sum += int(n[i]) * (2 ** (len(n) - 1 -i))