import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, n + 1)])
result = 0

for num in nums:
    left_index_cnt = [0, 0]
    right_index_cnt = [0, 0]

    while True:
        if deq[left_index_cnt[0]] == num:
            break
        left_index_cnt[0] += 1
        left_index_cnt[1] += 1
        if left_index_cnt[0] >= len(deq):
            left_index_cnt[0] += len(deq)

    while True:
        if deq[right_index_cnt[0]] == num:
            break
        right_index_cnt[0] -= 1
        right_index_cnt[1] += 1
        if right_index_cnt[0] < 0:
            right_index_cnt[0] += len(deq)
    
    if left_index_cnt[1] >= right_index_cnt[1] and right_index_cnt[1]:
        for _ in range(right_index_cnt[1]):
            deq.appendleft(deq.pop())
        result += right_index_cnt[1]
    elif left_index_cnt[1] < right_index_cnt[1] and left_index_cnt[1]:
        for _ in range(left_index_cnt[1]):
            deq.append(deq.popleft())
        result += left_index_cnt[1]
    deq.popleft()
print(result)