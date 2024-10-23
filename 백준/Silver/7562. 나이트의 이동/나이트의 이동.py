import sys
from collections import deque

def sol(b_r, s_x, s_y, g_x, g_y) -> int:
    movement = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    chessboard = [[-1] * b_r for _ in range(b_r)]
    queue = deque([(s_x, s_y)])
    chessboard[s_x][s_y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in movement:
            nx, ny = x + dx, y + dy
            if 0 <= nx < b_r and 0 <= ny < b_r:
                if chessboard[nx][ny] == -1:
                    chessboard[nx][ny] =  chessboard[x][y]+1
                    queue.append((nx, ny))
                    if nx == g_x and ny == g_y:
                        return chessboard[nx][ny]



test_cast = int(sys.stdin.readline())
for _ in range(test_cast):
    board_range = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    goal_x, goal_y = map(int, sys.stdin.readline().split())
    move_cnt = 0

    if start_x != goal_x or start_y != goal_y:
        move_cnt = sol(board_range, start_x, start_y, goal_x, goal_y)

    print(move_cnt)