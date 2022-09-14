# 왜 안되나
def solution(s):
    temp = s.split()
    ans = []
    for i in temp:
        ans.append(jadenWord(i))
    answer = ''
    for i in ans:
        answer += i
        answer += ' '
    return answer[:-1]

def jadenWord(s):
    return s[0].upper() + s[1:].lower()