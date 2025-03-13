def solution(word):
    from itertools import permutations

    strings = ["A","A","A","A","A", "E","E","E","E","E", "I","I","I","I","I", "O","O","O","O","O", "U","U","U","U","U", "", "", "", ""]
    arr = sorted(list(set([i[0] + i[1] + i[2] + i[3] + i[4] for i in permutations(strings, 5)])))
    answer = arr.index(word) + 1
    return answer