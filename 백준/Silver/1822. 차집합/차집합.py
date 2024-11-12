import sys

input = sys.stdin.readline

input()

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# b = [None] * (max(a) + 1)
# for i in a:
#     b[i] = 1
#
# for j in map(int, input().split()):
#     if b[j] and j < len(b):
#         b[j] -= 1
#
# result = 0
# result_list = []
# for k in range(len(b)):
#     if b[k]:
#         result += 1
#         result_list.append(k)
#
# print(result)
# print(' '.join(map(str, result_list)))

di ={}
result = []

for i in a:
    di[i] = 1

for i in b:
    if i in di:
        di[i] = 0

for i in di:
    if di[i] == 1:
        result.append(i)

result.sort()
print(len(result))
print(' '.join(map(str, result)))