def solution(sizes):
    answer = 0
    bigger = 0
    smaller = 0
    
    for size in sizes:
        bigger = max(bigger, max(size))
        smaller = max(smaller, min(size))
    answer = bigger * smaller
    return answer