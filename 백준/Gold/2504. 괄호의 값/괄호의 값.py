import sys

input = sys.stdin.readline

a = input().rstrip()
vps = []  # 스택
temp = 1   # 현재 괄호에 대한 계산을 위한 임시 변수
result = 0  # 최종 결과

for i in range(len(a)):
    if a[i] == "(":
        vps.append(a[i])
        temp *= 2  # (이 들어가면 temp를 2배로
    elif a[i] == "[":
        vps.append(a[i])
        temp *= 3  # [가 들어가면 temp를 3배로
    elif a[i] == ")":
        if vps and vps[-1] == "(":  # "("가 스택에 있어야 괄호 짝이 맞음
            vps.pop()
            if a[i-1] == "(":  # 직전이 "("라면 2배 값을 더해야 함
                result += temp
            temp //= 2  # 괄호를 닫았으니 temp를 2로 나누어줌
        else:
            result = 0
            break
    elif a[i] == "]":
        if vps and vps[-1] == "[":  # "["가 스택에 있어야 괄호 짝이 맞음
            vps.pop()
            if a[i-1] == "[":  # 직전이 "["라면 3배 값을 더해야 함
                result += temp
            temp //= 3  # 괄호를 닫았으니 temp를 3으로 나누어줌
        else:
            result = 0
            break

if vps:  # 스택에 남은 괄호가 있다면 잘못된 괄호가 존재하는 것
    result = 0

print(result)


# import sys
#
# input = sys.stdin.readline
#
# a = input().rstrip()
# vps = []
# temp = 1
# flag = 0
# result = 0
# for i in range(len(a)):
#     if a[i] == "(" or a[i] == "[":
#         if a[i] == "(":
#             temp *= 2
#         else:
#             temp *= 3
#         vps.append(a[i])
#         flag = len(vps)
#     elif vps != [] and (a[i] == ")" or a[i] == "["):
#         if vps[-1] == "(" and a[i] == ")":
#             if flag <= len(vps):
#                 result += temp
#             temp //= 2
#             vps.pop()
#         elif vps[-1] == "[" and a[i] == "]":
#             if flag <= len(vps):
#                 result += temp
#             temp //= 3
#             vps.pop()
#     else:
#         vps.append(a[i])
#         break
#
# if vps == []:
#     print(result)
# else:
#     print(0)