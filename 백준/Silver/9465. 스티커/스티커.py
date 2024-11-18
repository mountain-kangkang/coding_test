import sys

input = sys.stdin.readline

def dp(sticker, n) -> int:
    available = [[0] * n for _ in range(2)]

    available[0][0] = sticker[0][0]
    available[1][0] = sticker[1][0]
    if n == 1:
        return max(available[0][0], available[1][0])

    available[0][1] = sticker[1][0] + sticker[0][1]
    available[1][1] = sticker[0][0] + sticker[1][1]
    if n == 2:
        return max(available[0][1], available[1][1])

    for i in range(2, n):
        available[0][i] = max(available[1][i - 2], available[1][i - 1]) + sticker[0][i]
        available[1][i] = max(available[0][i - 2], available[0][i - 1]) + sticker[1][i]
    return max(available[0][n-1], available[1][n-1])

t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    print(dp(sticker, n))