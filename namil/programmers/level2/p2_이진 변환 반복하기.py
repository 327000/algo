# 채점 및 통과 완료
def solution(s):
    total_removing_zero_count = 0
    transition_count = 0
    numb_str = s
    while numb_str != '1':
        temp = transition(numb_str)
        numb_str = temp[0]
        transition_count += 1

        total_removing_zero_count += temp[1]

    answer = [transition_count, total_removing_zero_count]
    return answer


def transition(numb):
    one_count = 0  # 문자열 길이와 같을 것이다.
    zero_count = 0
    for i in numb:
        if i == '0':
            zero_count += 1
        elif i == '1':
            one_count += 1
    len_to_bin = bin(one_count)
    return [len_to_bin[2:], zero_count]  # [이진 변환 결과, 없앤 0 개수]
