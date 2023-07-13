# 달리기 경주 후 최종 순위를 담은 배열을 return

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

#풀이1
#인덱스를 이용한 풀이법
# def solution(players, callings):
#     for call in callings:
#             idx = players.index(call)
#             players[idx], players[idx-1] = players[idx-1], players[idx]
#     return players

#-> calling의 최대 길이가 1,000,000이고, players의 최대 길이가 50,000이기 때문에
#idx 하나를 구하기 위해선 1,000,000 * 50,000을 반복해야 한다.



#풀이2
#딕셔너리를 이용한 풀이: idx를 구하는 시간을 줄이기 위해 
#원래 인덱스로 접근하면 인덱스 하나하나 다 봐야하니까 최댓값으로 진행하게 되면 시간 너무 오래걸림. 그런데 딕셔너리 이용하면 해당 값 바로 찾을 수 있으니까 더 효율적인 것
def solution(players, callings):
    players_dict = {player:rank for rank,player in enumerate(players)} #선수명이 key
    # {'mumu':0, 'soe':1 , 'poe':2, 'kai':3, 'mine':4}
    rank_dict = {rank:player for rank,player in enumerate(players)} # 등수가 key
    # {0:'mumu', 1:'soe', 2:'poe', 3:'kai', 4:'mine'}
    
    #player와 rank의 두 개의 딕셔너리를 두는 이유는 키에 더 쉽게 접근하기 위해??
    for call in callings:
        idx = players_dict.get(call) 
        rank_dict[idx - 1], rank_dict[idx] = rank_dict[idx], rank_dict[idx -1]
        players_dict[rank_dict[idx - 1]], players_dict[rank_dict[idx]] = players_dict[rank_dict[idx]], players_dict[rank_dict[idx - 1]] # players_dict도 변경해줘야지 그 다음에 움직임!       
    return list(rank_dict.values()) #딕셔너리의 값을 리스트로 빼내는 법: list()로 감싸면 됨

print(solution(players, callings))