'''첫 번째 시도: 효율성 3,4통과 못함(해시문제인제 해시를 전혀 안씀)
def solution(phone_book):
    phone_book.sort()

    while True:
        p = phone_book.pop(0)
        for phone in phone_book:
            if phone.startswith(p):
                return False
        if len(phone_book) == 1:
            return True
정답과 차이: 나는 내 값으로 중복값 찾으려 했는데 정답은 나 이외에 중복값이 있는지 보는 것

**문자열의 숫자를 오름차순으로 sort하는 법**
그냥 list.sort()하면 오류 발생
list.sort(key = int) 안됨 sorted(list, key = int)시 가능

'''

def solution(phoneBook):
    dic = {}

    for phone_number in phoneBook: #딕셔너리에 전화번호 넣기
        dic[phone_number] = 1
        
    for phone_number in phoneBook:
        temp = ''
        for number in phone_number: ## 한번에 temp = phone_number로 받아서 비교하면 자기 자신 뺄 수 없음 문자열 하나씩 넣어서 만들어주는것
            temp += number
            if temp in dic and temp != phone_number: ## temp == phone_number면 자기자신이니까
                return False
    return True

print(solution(["12","123","1235","567","88"]))