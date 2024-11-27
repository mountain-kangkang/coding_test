import sys

input = sys.stdin.readline
print = sys.stdout.write

def solve_post_office_location(n, villages):
    # 마을을 위치 순으로 정렬
    villages.sort(key=lambda x: x[0])

    # 전체 인구 계산
    total_population = sum(people for _, people in villages)

    # 누적 인구 계산
    cumulative_population = 0

    for location, people in villages:
        cumulative_population += people

        # 누적 인구가 전체 인구의 절반 이상이 되는 지점 찾기
        if cumulative_population >= (total_population + 1) // 2:
            return location

    return villages[-1][0]  # 마지막 마을 위치 반환

# 입력 처리
n = int(input())
villages = [tuple(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(str(solve_post_office_location(n, villages)))

# n = int(input())
#
# village = []
# result = 0
# for _ in range(n):
#     a, b = map(int, input().split())
#     village.append(b)
#     result += ((a-1) * b)
#
# idx = 1
# result -= village[0]
# for i in range(len(village)):
#     temp = result + sum(village[:i]) - sum(village[i:])
#     if temp < result:
#         result = temp
#         idx = i + 1
# print(str(idx))