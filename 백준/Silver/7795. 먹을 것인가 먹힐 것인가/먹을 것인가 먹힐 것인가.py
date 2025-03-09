# import sys
#
# input = sys.stdin.readline
#
# t = int(input())
#
# def A_bigger_than_B() -> int:
#     nm = list(map(int, input().split()))
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     A.sort()
#     B.sort()
#
#     result = 0
#     for i in range(nm[0]):
#         for ii in range(nm[1]):
#             if A[i] > B[ii]:
#                 result += 1
#             else:
#                 break
#
#     return result
#
# for _ in range(t):
#     print(A_bigger_than_B())

"""
해당 코드의 시간 복잡도를 줄이기 위해서는 두 개의 배열 A와 B에서 각각의 원소가 다른 배열의 원소보다 큰 경우를 효율적으로 찾는 방법을 사용해야 합니다.
현재 코드는 시간 복잡도가 O(n×m)입니다. 이를 개선하기 위해 이분 탐색을 활용할 수 있습니다.
"""

# import sys
# import bisect
# 
# input = sys.stdin.readline
# 
# t = int(input())
# 
# 
# def A_bigger_than_B() -> int:
#     nm = list(map(int, input().split()))
#     A = sorted(map(int, input().split()))
#     B = sorted(map(int, input().split()))
# 
#     result = 0
#     for a in A:
#         # B에서 a보다 큰 수의 개수는 B에서 a보다 작은 수의 개수를 빼면 된다.
#         # bisect.bisect_right(B, a)로 a보다 큰 수의 개수를 구할 수 있다.
#         result += nm[1] - bisect.bisect_right(B, a)
# 
#     return result
# 
# 
# for _ in range(t):
#     print(A_bigger_than_B())

"""
1. 이분 탐색 사용: bisect 모듈의 bisect_right 함수를 사용하여 B 배열에서 a보다 큰 수의 개수를 효율적으로 찾습니다.
    이는 O(log m) 시간 복잡도로 수행됩니다.

2. 시간 복잡도 개선: 전체 시간 복잡도는 O(nlogm)로 개선됩니다.
    이는 n번의 이분 탐색을 수행하기 때문입니다.
"""

import sys
import bisect

input = sys.stdin.readline

t = int(input())


def A_bigger_than_B() -> int:
    nm = list(map(int, input().split()))
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    result = 0
    for b in B:
        # B에서 a보다 큰 수의 개수는 B에서 a보다 작은 수의 개수를 빼면 된다.
        # bisect.bisect_right(B, a)로 a보다 큰 수의 개수를 구할 수 있다.
        result += nm[0] - bisect.bisect_right(A, b)

    return result


for _ in range(t):
    print(A_bigger_than_B())