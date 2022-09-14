def solution(s):
    word_list = s.split()
    ans_word_list = []

    for i in word_list:
        if len(i) > 1:
            ans_word_list.append(i[0].upper() + i[1:].lower())
        elif len(i) == 1:
            ans_word_list.append(i[0].upper())
        elif i == ' ':
            pass


    return ' '.join(ans_word_list)