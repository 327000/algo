# n진수 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17687?language=python3
def solution(n, t, m, p):
    game = ''
    numb_now = 0

    while len(game) <= t * m:
        game += numbify(n, numb_now)
        numb_now += 1
    answer = game[p-1::m]
    return answer[:t]

def numbify(n:int, x:int):
    answer = ''
    temp = x
    if temp < n:
        return moreThanTen(temp)
    while temp >= n:
        answer = moreThanTen(temp % n) + answer
        temp = temp // n
        if not temp >= n:
            answer = moreThanTen(temp) + answer
        else:
            continue
    return answer

def moreThanTen(x:int):
    if x == 10:
        return 'A'
    elif x == 11:
        return 'B'
    elif x == 12:
        return 'C'
    elif x == 13:
        return 'D'
    elif x == 14:
        return 'E'
    elif x == 15:
        return 'F'
    else:
        return str(x)