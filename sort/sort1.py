def solution(array, commands): ##내코드
    answer = []
    for com in commands:
        temp = sorted(array[com[0]-1:com[1]])
        answer.append(temp[com[2]-1])

    return answer

def solution(array, commands): ## map, lambda이용한 코드
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

##map(함수,리스트) : 리스트로부터 원소를 하나씩 꺼내서 함수에 적용시킨다음, 그 결과를 새로운 리스트로 담아줌 **인자값2개**



print(solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]]))
