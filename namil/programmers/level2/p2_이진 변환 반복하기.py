def solution(s):
    temp_numb = s
    total_zero_count = 0
    trans_count = 0
    while temp_numb != '1':
        temp_trans = transition(temp_numb)  # temp_trans is a list. [transition, zero_count]
        trans_count += 1
        temp_numb = temp_trans[0]
        total_zero_count += temp_trans[1]
    answer = [trans_count, total_zero_count]
    return answer

def transition(numb:str):
    numb_list = numb.split()
    ans1 = ''
    zero_count = 0
    for i in numb_list:
        if i == "0":
            zero_count += 1
        elif i == "1":
            ans1 = ans1 + i

    ans2 = len(ans1)
    return [bin(ans2)[2:], zero_count]