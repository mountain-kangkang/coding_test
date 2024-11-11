import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
ij = [list(map(int, input().split())) for _ in range(n)]

def bfs(matrix, size):
    root = [[0] * size for _ in range(size)]
    direct = deque([])
    for i in range(size):
        [direct.append(j) for j in range(size) if matrix[i][j] == 1]
        while direct:
            direction = direct.popleft()
            root[i][direction] = 1
            for j in range(size):
                if matrix[direction][j] == 1 and root[i][j] == 0:
                    root[i][j] = 1
                    direct.append(j)

    return root

for i in bfs(ij, n):
    for j in i:
        sys.stdout.write(str(j) + ' ')
    sys.stdout.write('\n')