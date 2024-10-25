import sys
from collections import deque

n = int(sys.stdin.readline())
lope_pwr = deque(sorted([int(sys.stdin.readline()) for _ in range(n)]))

result = []
while lope_pwr:
    result.append(lope_pwr[0] * len(lope_pwr))
    lope_pwr.popleft()

print(max(result))