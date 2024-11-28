from collections import deque
import sys
input = sys.stdin.readline
MIN = -int(1e9)
MAX = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist_ans = MIN
min_ans = MAX
count_ans = 0

def bfs(start, d):
    global dist_ans, count_ans, min_ans
    q = deque()
    q.append((start, d))
    while q:
        now, dist = q.popleft()
        visited[now] = True
        if dist_ans < dist:
            min_ans = now
            dist_ans = dist
            count_ans = 1
        elif dist_ans == dist:
            min_ans = min(min_ans, now)
            count_ans += 1
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist+1))
bfs(1, 0)
print(min_ans, dist_ans, count_ans)

# import sys
# from collections import deque
#
# input = sys.stdin.readline
# print = sys.stdout.write
#
# n, m = map(int, input().split())
#
# barn = [[0] * n for _ in range(n)]
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     barn[x-1][y-1] = 1
#     barn[y-1][x-1] = 1
#
# def bfs(barn, n):
#     q = deque([(0, i) for i in range(n) if barn[0][i] == 1])
#     distance = [0] * n
#
#     while q:
#         idx, next_idx = q.popleft()
#         if distance[next_idx] == 0 or distance[next_idx] > distance[idx] + 1:
#             distance[next_idx] = distance[idx] + 1
#             for i in range(1, n):
#                 if barn[next_idx][i] == 1 and distance[i] == 0 or distance[i] > distance[next_idx] + 1:
#                     q.append((next_idx, i))
#
#     max_num = max(distance)
#     max_idx = distance.index(max_num)
#     max_cnt = distance.count(max_num)
#     print(f"{max_idx+1} {max_num} {max_cnt}\n")
#
# bfs(barn, n)