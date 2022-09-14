# 통과
def solution(brown, yellow):
    yellow_w = yellow

    while 1:
        if yellow % yellow_w == 0:
            yellow_h = yellow // yellow_w
            if brown == (2 * (yellow_w + yellow_h)) + 4:
                return [yellow_w+2, yellow_h+2]
            else:
                yellow_w -= 1
        else:
            yellow_w -= 1