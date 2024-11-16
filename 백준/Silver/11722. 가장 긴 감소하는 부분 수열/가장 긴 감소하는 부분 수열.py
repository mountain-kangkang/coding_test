import sys

input = sys.stdin.readline

# def main():
#     n = int(input())
#     a = list(map(int, input().split()))
#     result = [0] * n
#
#     for i in range(n):
#         length = 1
#         temp = a[i]
#         for j in range(i-1, -1, -1):
#             if a[j] > temp:
#                 temp = a[j]
#                 length += 1
#         result[i] = length
#     print(max(result))
def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = [1] * n  # 각 인덱스에서 시작하는 감소하는 부분 수열의 최소 길이는 1

    for i in range(1, n):  # i번째 원소부터 시작
        for j in range(i - 1, -1, -1):  # i 이전의 원소들과 비교
            if a[j] > a[i]:  # a[j]가 a[i]보다 크면
                result[i] = max(result[i], result[j] + 1)  # result[i]를 갱신
    print(max(result))  # 가장 긴 감소하는 부분 

if __name__ == '__main__':
    main()
    sys.exit(0)

'''
8
70 19 18 17 16 22 21 20
5
5 4 3 2 1
'''
