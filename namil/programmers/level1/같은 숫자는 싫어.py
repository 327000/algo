def solution(arr):
    answer = []

    for i in arr:
        if answer:
            if answer[len(answer) - 1] == i:
                pass
            else:
                answer.append(i)
        else:
            answer.append(i)

    return answer