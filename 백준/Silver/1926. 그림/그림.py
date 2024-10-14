import sys
from collections import deque

def bfs(painting, start_x, start_y, m, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_x, start_y)])
    painting[start_y][start_x] = 2  # Visited mark
    size = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and painting[ny][nx] == 1:
                painting[ny][nx] = 2  # Visited mark
                queue.append((nx, ny))
                size += 1
    return size

n, m = map(int, sys.stdin.readline().split())
painting = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

if all(all(paint == 0 for paint in row) for row in painting):
    print(0)
    print(0)
else:
    num_of_paintings = 0
    max_size = 0

    for y in range(n):
        for x in range(m):
            if painting[y][x] == 1:  # Found an unvisited painting
                num_of_paintings += 1
                size = bfs(painting, x, y, m, n)
                max_size = max(max_size, size)

    print(num_of_paintings)
    print(max_size)
