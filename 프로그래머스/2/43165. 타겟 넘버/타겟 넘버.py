from itertools import combinations

def solution(numbers, target):
    answer = 0
    need = (sum(numbers) - target) // 2

    for i in range(1, len(numbers)+1):
        combi = combinations(numbers, i)
        for comb in combi:
            if sum(comb) == need:
                answer += 1

    return answer