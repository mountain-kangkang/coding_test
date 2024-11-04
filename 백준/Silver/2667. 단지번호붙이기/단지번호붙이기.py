import sys
from collections import deque

input = sys.stdin.readline

def sol(apt, c_fla, x, y):
    global vir_apt
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    vir_apt[x][y] = c_fla
    deq = deque([(x, y)])
    cnt = 1

    while deq:
        x, y = deq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(apt) and 0 <= ny < len(apt) and apt[nx][ny] == 1 and vir_apt[nx][ny] == -1:
                vir_apt[nx][ny] = c_fla
                cnt += 1
                deq.append((nx, ny))
    return  cnt

n = int(input())
apt = []
for i in range(n):
    temp = [int(m) for m in input().rstrip()]
    apt.append(temp)

vir_apt = [[-1] * n for _ in range(n)]
cnt_flag = 0
cnt = []
for i in range(n):
    for j in range(n):
        if vir_apt[i][j] == -1 and apt[i][j] == 1:
            cnt_flag += 1
            cnt.append(sol(apt, cnt_flag, i, j))
print(cnt_flag)
cnt.sort()
[print(i) for i in cnt]