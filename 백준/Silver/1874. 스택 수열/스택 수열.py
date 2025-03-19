# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
#
# stack_ = deque([i for i in range(1, n+1)])
# temp = []
# result = []
#
# for _ in range(n):
#     find_num = int(input())
#
#     if (find_num not in temp) and (find_num not in stack_):
#         print("NO")
#         sys.exit()
#
#     if stack_ != deque():
#         while stack_[0] <= find_num:
#             temp.append(stack_.popleft())
#             result.append("+")
#             if stack_ == deque():
#                 break
#     if temp != []:
#         while temp[-1] >= find_num:
#             temp.pop()
#             result.append("-")
#             if temp == []:
#                 break
#
# print(*result, sep="\n")

import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []
current = 1  # 다음에 스택에 넣을 숫자

for _ in range(n):
    target = int(input())

    # 현재 숫자부터 target까지 스택에 push
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1

    # 스택 top이 target과 같은지 확인
    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit(0)

print('\n'.join(result))
