def solution(id_list, report, k):
    reported_count = {id1: {id2: 0 for id2 in id_list} for id1 in id_list}

    mailed_count = {}
    for i in id_list:
        mailed_count[i] = 0

    for i in report:
        reporter, target = i.split()
        if reported_count[target][reporter] != 0 or target == reporter:
            pass
        else:
            reported_count[target][reporter] = 1

    for i in id_list:
        reporter_list = []

        for j in id_list:
            if reported_count[i][j] == 1:
                reporter_list.append(j)

        if len(reporter_list) >= k:
            for i in reporter_list:
                mailed_count[i] += 1

    answer = list(mailed_count.values())

    return answer
