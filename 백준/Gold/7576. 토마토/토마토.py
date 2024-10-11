import sys
from collections import deque

def bfs(tomato_box, m, n):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ripe_positions = deque()
    
    # 익은 토마토의 초기 위치를 큐에 추가
    for y in range(n):
        for x in range(m):
            if tomato_box[y][x] == 1:
                ripe_positions.append((x, y))

    days = 0  # 날짜 카운트

    while ripe_positions:
        for _ in range(len(ripe_positions)):
            row, column = ripe_positions.popleft()
            for dx, dy in directions:
                nx, ny = row + dx, column + dy
                if 0 <= nx < m and 0 <= ny < n and tomato_box[ny][nx] == 0:
                    tomato_box[ny][nx] = 1  # 익게 만든다
                    ripe_positions.append((nx, ny))
        
        days += 1  # 하루가 지나면

    # 모든 토마토가 익었는지 확인
    for row in tomato_box:
        if 0 in row:  # 익지 않은 토마토가 있다면
            return -1

    return days - 1  # 마지막에 익은 날 수에서 1을 빼줌

m, n = map(int, sys.stdin.readline().split())
tomato_box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

if all(all(tomato != 0 for tomato in row) for row in tomato_box):
    print(0)
else:
    result = bfs(tomato_box, m, n)
    print(result)
