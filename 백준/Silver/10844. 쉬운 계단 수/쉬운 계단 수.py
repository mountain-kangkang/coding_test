import sys
input = sys.stdin.readline

MOD = 1000000000

# 길이 N (1 <= N <= 100) 에 대한 계단수의 개수를 구하는 함수
def count_stair_numbers(N):
    # dp[n][i] -> 길이가 n이고 끝자리가 i인 계단수의 개수
    dp = [[0] * 10 for _ in range(N + 1)]

    # 초기 조건: 길이가 1인 계단수는 1부터 9까지
    for i in range(1, 10):
        dp[1][i] = 1

    # DP 계산
    for n in range(2, N + 1):
        for i in range(10):
            if i - 1 >= 0:
                dp[n][i] += dp[n - 1][i - 1]
            if i + 1 < 10:
                dp[n][i] += dp[n - 1][i + 1]
            dp[n][i] %= MOD  # 큰 수를 처리하기 위해 나머지 연산

    # 길이가 N인 계단수의 합을 구합니다
    result = sum(dp[N]) % MOD
    return result

# 입력 받기
N = int(input())

# 결과 출력
print(count_stair_numbers(N))
