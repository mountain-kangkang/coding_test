import sys

n = int(sys.stdin.readline())
level_point = [int(sys.stdin.readline()) for _ in range(n)]

result = 0
for i in range(n-2, -1, -1):
    if level_point[i] >= level_point[i+1]:
        temp = level_point[i] - level_point[i+1] + 1
        result += temp
        level_point[i] -= temp

print(result)