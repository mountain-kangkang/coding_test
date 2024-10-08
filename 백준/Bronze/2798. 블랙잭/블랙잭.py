import sys

N, M = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))
if N != len(card_list):
    print("error")

result = ()

def solution(num):
    global N, M, card_list, result
    if num == N - 2:
        return

    for i in range(1 + num, N - 1):
        for j in range(i + 1, N):
            if result == () and (M - (card_list[num]+card_list[i]+card_list[j])) >= 0:
                result = ((card_list[num]+card_list[i]+card_list[j]), M - (card_list[num]+card_list[i]+card_list[j]))
                # print(card_list[num], card_list[i], card_list[j], result[1])
                continue
            if (M - (card_list[num]+card_list[i]+card_list[j])) >= 0:
                if result[1] > (M - (card_list[num]+card_list[i]+card_list[j])):
                    result = ((card_list[num]+card_list[i]+card_list[j]), M - (card_list[num]+card_list[i]+card_list[j]))
                    # print(card_list[num], card_list[i], card_list[j], result[1])
                    continue
    solution(num + 1)

solution(0)

print(result[0])