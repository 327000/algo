# 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1.upper()
    str2.upper()
    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() == False or str1[i+1].isalpha() == False:
            pass
        else:
            str1_list.append(str1[i].upper() + str1[i+1].upper())

    for i in range(len(str2) - 1):
        if str2[i].isalpha() == False or str2[i+1].isalpha() == False:
            pass
        else:
            str2_list.append(str2[i].upper() + str2[i+1].upper())

    intersection = []
    total = []

    while str1_list:
        temp = str1_list.pop()
        total.append(temp)
        if temp in str2_list:
            intersection.append(temp)
            str2_list.remove(temp)
        else:
            pass

    total += str2_list

    if total:
        answer = len(intersection) / len(total)
    else:
        answer = 1

    return int(answer * 65536)