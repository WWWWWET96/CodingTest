import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())
    '''문제에서 단 한명의 선수만 완주하지못했다고 했으니까 [0]붙인 것
    [0]제외하고 제출하면 시간 에러 나는듯'''
solution(["leo", "kiki", "eden","lee"], ["eden", "kiki"])