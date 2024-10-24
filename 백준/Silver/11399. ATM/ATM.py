import sys

n = int(sys.stdin.readline())
p = sorted(list(map(int, sys.stdin.readline().split())))

result = []
for i in range(n):
    result.append(sum(p[:i +1]))

print(sum(result))