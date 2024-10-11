# https://acmicpc.net/problem/2583
import sys

def solution():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    m, n, k = map(int, sys.stdin.readline().split())
    land = [[1] * n for _ in range(m)]

    territory = set()
    for _ in range(k):
        x1, y1, x2, y2 = map(int, sys. stdin. readline().split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                land[y][x] = 0
    for x in range(n):
        for y in range(m):
            if land[y][x]:
                territory.add((x, y))
    
    areas = []

    while territory:
        spot = [territory.pop()]
        area = 0
        
        while spot:
            x, y = spot.pop()
            area += 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (nx, ny) in territory:
                    territory.discard((nx, ny))
                    spot.append ((nx, ny))
        areas.append(area)

    print(len(areas))
    areas.sort()
    [print(area, end=" ") for area in areas]
    print()

solution ()