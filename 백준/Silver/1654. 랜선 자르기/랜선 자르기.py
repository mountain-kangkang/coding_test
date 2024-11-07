import sys

input = sys.stdin.readline

def can_cut(cables, target_length, target_count):
    total_cables = 0
    for cable in cables:
        total_cables += cable // target_length
    return total_cables >= target_count

def binary_search(cables, target_count, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if can_cut(cables, mid, target_count):
            result = mid  # 가능한 길이 중에서 가장 큰 값을 찾음
            start = mid + 1  # 더 긴 길이를 시도
        else:
            end = mid - 1  # 너무 긴 길이를 줄여야 함
    return result

k, n = map(int, input().split())  # K: 기존 랜선의 개수, N: 필요한 랜선의 개수
cables = [int(input()) for _ in range(k)]  # K개의 랜선 길이 입력

# 이진 탐색을 통해 가장 긴 랜선 길이를 찾음
result = binary_search(cables, n, 1, max(cables))

print(result)