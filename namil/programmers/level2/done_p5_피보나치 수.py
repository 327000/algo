# 통과
def solution(n):
    f_n_minus_2 = 0
    f_n_minus_1 = 1
    f_n = 0
    for i in range(n-1):
        f_n = f_n_minus_1 + f_n_minus_2
        f_n_minus_2 = f_n_minus_1
        f_n_minus_1 = f_n
    print(f_n)
    answer = f_n % 1234567
    return answer
