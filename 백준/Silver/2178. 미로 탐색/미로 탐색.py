import sys
from collections import deque

def bfs(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    distances = [[-1] * m for _ in range(n)]  # 거리 배열 초기화
    distances[0][0] = 1  # 시작점까지의 거리는 1

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1:
                if distances[ny][nx] == -1:  # 방문하지 않은 경우
                    distances[ny][nx] = distances[y][x] + 1
                    queue.append((nx, ny))
                    if nx == m - 1 and ny == n - 1:  # 도착점에 도달한 경우
                        return distances[ny][nx]

    return -1  # 도착할 수 없는 경우

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

result = bfs(maze, n, m)
print(result)
