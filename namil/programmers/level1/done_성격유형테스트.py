def solution(survey, choices):
    answer = ''
    dic = {'indR': 0, 'indT': 0, 'indC': 0, 'indF': 0, 'indJ': 0, 'indM': 0, 'indA': 0, 'indN': 0}

    for i in range(len(survey)):
        if choices[i] <= 3:
            dic['ind' + survey[i][0]] += 4 - choices[i]
        elif choices[i] >= 5:
            dic['ind' + survey[i][1]] += choices[i] - 4

    if dic['indR'] >= dic['indT']:
        answer += 'R'
    else:
        answer += 'T'

    if dic['indC'] >= dic['indF']:
        answer += 'C'
    else:
        answer += 'F'

    if dic['indJ'] >= dic['indM']:
        answer += 'J'
    else:
        answer += 'M'

    if dic['indA'] >= dic['indN']:
        answer += 'A'
    else:
        answer += 'N'

    return answer
