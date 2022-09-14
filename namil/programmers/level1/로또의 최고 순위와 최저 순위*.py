def solution(lottos, win_nums):
    win_count = 0
    zero_count = 0

    for i in lottos:
        if i == 0:
            zero_count += 1
        elif i in win_nums:
            win_count += 1

    max_win = win_count + zero_count
    min_win = win_count

    answer = []

    if max_win <= 1:
        answer = [6, 6]
    elif min_win <= 1:
        answer = [7 - max_win, 6]
    else:
        answer = [7 - max_win, 7 - min_win]

    return answer