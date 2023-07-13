# n번째에 해당되는 피보나치 수열의 숫자 구하는 함수

# #풀이1: 재귀함수 돌려서 값 찾기
# def solution(n):
#     if(n == 1 or n == 2):
#         return 1
#     return solution(n - 1) + solution(n - 2)
#숫자가 커질수록 기존 계산한 함수의 값을 또 계산하게 되니까 시간 오래걸림
# -> 기존 계산한 함수는 저장해두기

#풀이2:한 번 계산한 결과는 저장해두도록
memo = {1:1, 2:1} # 초기값은 n=1이거나 2일 때 1 반환하도록

def solution(n):
    if n in memo:
        return memo[n]
    memo[n] = solution(n-1) + solution(n-2)
    return memo[n]

print(solution(6))