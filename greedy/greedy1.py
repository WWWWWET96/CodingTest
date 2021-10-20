'''
탐욕 알고리즘: 매 순간 최적이라고 생각되는 경우를 선택하는 방식으로 진행
리스트 비어있는지? len(list) == 0 -> 파이썬스럽지않음
if not list:
    print("list is empty")

리스트 reserve의 방식
1. list.reverse()는 아무런 값도 반환하지 않음
2. reversed(list)는 순서가 거꾸로 뒤집힌 리스트 반환
-> 하지만 그냥 print(reversed(list))하면 x
list(reversed(list))해야 list가 뒤집힌 list반환
'''
def solution(n, lost, reserve):
    answer = n -len(lost)
    lost.reverse()
    reserve.reverse()
    while True:
        if (not lost) | (not reserve): return answer
        lo = lost.pop()
        re = reserve.pop()
        if lo-1 == re:
            answer += 1
        elif lo +1 == re:
                answer += 1

    return answer

print(solution(5, [2,4], [1,3,5]))