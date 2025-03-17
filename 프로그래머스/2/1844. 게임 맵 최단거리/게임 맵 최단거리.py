from collections import deque

# def solution(maps):
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque([(0, 0)])
#     m, n = len(maps[0]), len(maps)
#     distances = [[-1] * m for _ in range(n)]  # 거리 배열 초기화
#     distances[0][0] = 1  # 시작점까지의 거리는 1

#     while queue:
#         x, y = queue.popleft()

#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
#                 if distances[ny][nx] == -1:  # 방문하지 않은 경우
#                     distances[ny][nx] = distances[y][x] + 1
#                     queue.append((nx, ny))
#                     if nx == m - 1 and ny == n - 1:  # 도착점에 도달한 경우
#                         return distances[ny][nx]

#     return -1  # 도착할 수 없는 경우

def solution(maps):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    sero, garo = len(maps), len(maps[0])
    location = [[-1] * garo for _ in range(sero)]
    location[0][0] = 1

    while queue:
        current_location_sero, current_location_garo = queue.popleft()

        for direction_sero, direction_garo in direction:
            next_location_sero, next_location_garo = current_location_sero + direction_sero, current_location_garo + direction_garo

            if 0 <= next_location_sero < sero and 0 <= next_location_garo < garo:   # map의 범위를 벗어나는지 확인
                if maps[next_location_sero][next_location_garo] == 1:               # 확인할 좌표가 갈 수 있는 길인지 확인
                    if location[next_location_sero][next_location_garo] == -1:      # 아직 방문하지 않은 좌표인지 확인
                        location[next_location_sero][next_location_garo] = location[current_location_sero][current_location_garo] + 1   # 현재 좌표에서 +1 하여 저장해서 거리 계산

                        if next_location_sero == sero - 1 and next_location_garo == garo - 1:   # 만약 다음 좌표가 목표 지점이라면 그 거리를 반환하며 함수 종료
                            return location[next_location_sero][next_location_garo]

                        queue.append((next_location_sero, next_location_garo))

    return -1