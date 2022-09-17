# 통과
def solution(n, words):
    already = []
    wrong_word_numb = 0
    word_before = ''
    for i in words:
        wrong_word_numb += 1
        if wrong_word_numb == 1:
            already.append(i)
            word_before = i
        else:
            if i in already or i[0] != word_before[-1]:
                if wrong_word_numb % n == 0:
                    print(wrong_word_numb)
                    return [n, wrong_word_numb // n]
                else:
                    print(wrong_word_numb)
                    return [wrong_word_numb % n, wrong_word_numb // n +1]
            else:
                already.append(i)
                word_before = i
    return [0, 0]
