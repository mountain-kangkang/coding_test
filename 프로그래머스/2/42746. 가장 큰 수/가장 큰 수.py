# from itertools import permutations


# def solution(numbers):
#     temp = sorted([''.join(num) for num in permutations((map(str, numbers)), len(numbers))])
#     return temp[-1]
# 테스트 케이스 1~11번 시간초과

# def solution(numbers):
#     temp = list(reversed(sorted(list(map(str, numbers)))))
#     temp2 = []
#     for num in permutations(temp, len(numbers)):
#         temp2.append("".join(num))
#         if int(num[0]) < int(temp[0][0]):
#             break
#     temp2.sort()
#     return temp2[-1]
# 테스트 케이스 1~11번 시간초과 위 함수보다 시간이 3배 더 걸림

def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))

    # 정렬 기준: x+y > y+x 이면 x가 y보다 앞에 와야 함
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 모든 숫자가 0인 경우 예외 처리
    return str(int(''.join(numbers)))