# https://www.acmicpc.net/problem/1012

import sys
from collections import deque

def farming(row:int, column:int, ea:int):
    global farm
    temp = [0] * row
    farm = [[0] * row for _ in range(column)]

    for i in range(ea):
        x, y = map(int, sys.stdin.readline().split())
        farm[y][x] = 1

def bfs(start_row, start_column):
    global N, M, farm
    queue = deque([(start_row, start_column)])
    farm[start_column][start_row] = 0  # 방문 처리

    while queue:
        row, column = queue.popleft()
        # 상하좌우 탐색
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_column = row + dr, column + dc
            if 0 <= new_row < M and 0 <= new_column < N and farm[new_column][new_row] == 1:
                farm[new_column][new_row] = 0  # 방문 처리
                queue.append((new_row, new_column))

T = int(sys.stdin.readline())

for _ in range(T):
    farm = []
    M, N, K = map(int, sys.stdin.readline().split())    # 가로, 세로, 개수
    farming(M, N, K)

    result = 0
    for column in range(N):
        for row in range(M):
            if farm[column][row]:
                bfs(row, column)
                result += 1
    print(result)

    