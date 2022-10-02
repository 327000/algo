# 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities:list):
    if cacheSize == 0:
        return len(cities) * 5

    cache_list = []
    answer = 0
    lll = []

    for i in cities:
        lll.append(i.upper())

    while lll:
        temp = lll.pop(0)
        if temp in cache_list:
            cache_list.remove(temp)
            cache_list.append(temp)
            answer += 1
        elif len(cache_list) < cacheSize:
            cache_list.append(temp)
            answer += 5
        else:
            answer += 5
            cache_list.pop(0)
            cache_list.append(temp)

    return answer