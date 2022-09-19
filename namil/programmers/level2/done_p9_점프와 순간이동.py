# 점프와 순간이동
# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    efficient_battery = 0
    dist_left = n
    while dist_left != 0:
        temp = jumpOrTeleport(dist_left, 0)
        efficient_battery = temp[1]
        dist_left = temp[0]
    return efficient_battery


def jumpOrTeleport(n, battery):
    if n == 0:
        return [0, battery]
    elif n % 2 == 0:
        return jumpOrTeleport(n // 2, battery)
    else:
        return jumpOrTeleport(n - 1, battery + 1)