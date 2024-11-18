import sys

input = sys.stdin.readline

def dp(sticker, n) -> int:
    DP = [[0] * n for _ in range(2)]

    DP[0][0] = sticker[0][0]
    DP[1][0] = sticker[1][0]
    if n == 1:
        return max(DP[0][0], DP[1][0])

    DP[0][1] = sticker[1][0] + sticker[0][1]
    DP[1][1] = sticker[0][0] + sticker[1][1]
    if n == 2:
        return max(DP[0][1], DP[1][1])

    for i in range(2, n):
        DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + sticker[0][i]
        DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + sticker[1][i]
    return max(DP[0][n-1], DP[1][n-1])

t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    print(dp(sticker, n))