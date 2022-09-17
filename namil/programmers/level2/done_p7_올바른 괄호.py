# 효율성 실패
# def solution(s):
#     temp = []
#
#     if len(s) % 2 != 0:
#         return False
#
#     for i in s:
#         if i == '(':
#             temp.append('(')
#         elif i == ')':
#             if temp:
#                 temp.remove('(')
#             else:
#                 return False
#
#     if temp:
#         return False
#     else:
#         return True

# 통과
def solution(s):
    s_list = list(s)
    close_stack = []

    while s_list:
        temp = s_list.pop()
        if temp == ')':
            close_stack.append(temp)
        elif temp == '(':
            if close_stack:
                close_stack.pop()
            else:
                return False

    if close_stack:
        return False
    else:
        return True
