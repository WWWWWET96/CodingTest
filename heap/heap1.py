#제일 작은 수 제일 큰 수: 힙(완전이진트리 O(logN)) 생각 -> 리스트 heap으로
#문제 제대로 읽어야함 이해잘못해서 테스트통과못했었음
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K: break
        if len(scoville) == 0: return -1 #더이상 계산불가
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2) #list.append와 달리 최소합으로 맞춰짐
        answer += 1

    return answer


print(solution([1,1,1,1,1], 7))