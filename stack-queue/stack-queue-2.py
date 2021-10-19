'''큐 리스트로도 구현 하지만 pop, insert시 성능적으로 불리한 연산
que: 멀티스레드 환경에서 스레드 간의 안전한 소통위해 만들어진 라이브러리
deque: 양방향에서 삽입 삭제 일어나는 자료구조
        list와 비슷하게 동작하지만 삽입 삭제에 있어어deque가 동작 더 빠르게 수행'''

'''내 풀이: 런타임에러 남 
from collections import deque
def solution(priorities ,location):
    que = deque()
    for p in priorities:
        que.append(p)
    answer = 0 #언제 출력되는지 알기위해

    while len(que) != 0:
        temp = que.popleft()
        if temp < max(que):
            que.append(temp)
            if location == 0: location= len(que) -1
            else: location -= 1

        else: # 출력될 때
            if location == 0: return answer+1 # 원하던게 출력된 것
            else:
                location -= 1
                answer += 1

print(solution([1,3,4,4,2], 4))'''

def solution(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)] ## queque에 [(idx, value)] 형태로 저장
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):## any: 요소중에 하나라도 True있으면 True 리턴,전부 다 False이면 False 반환
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution([1,3,4,4,2], 4))