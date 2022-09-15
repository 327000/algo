# 통과
def solution(sizes):
    for i in sizes:
        w = i[0]
        h = i[1]
        if i[0] < i[1]:
            i[0] = h
            i[1] = w
    w_max = 0
    h_max = 0
    for i in sizes:
        if w_max < i[0]:
            w_max = i[0]
        if h_max < i[1]:
            h_max = i[1]
    return w_max * h_max


# 8, 15랑 14, 7하면 14 15
# 60 50, 70 30, 60 30, 80 40
#