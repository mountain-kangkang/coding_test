import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# a를 내림차순으로 정렬
a.sort(reverse=True)

# b를 정렬한 인덱스를 찾기
indexed_b = sorted(range(n), key=lambda i: b[i])

# 최종 결과 계산
result = sum(a[i] * b[indexed_b[i]] for i in range(n))

print(result)
