#통과
def solution(s):
    s_list = list(map(int, s.split()))

    a_min = s_list[0]
    a_max = s_list[0]

    for i in s_list:
        if i < a_min:
            a_min = i
        if i > a_max:
            a_max = i

    return str(a_min) + " " + str(a_max)