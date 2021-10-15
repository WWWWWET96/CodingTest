from math import ceil
def solution(progresses, speeds):
    list , answer = [],[]
    for p,s in zip(progresses,speeds):
        list.append(ceil((100-p)/s))

    temp, count = list[0],1

    for a in list[1:]:
        if(temp >= a):
            count += 1
        else:
            answer.append(count)
            count = 1
            temp = a
    answer.append(count)#제일 마지막 원소의 일수 넣기위해
    return answer


print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))

