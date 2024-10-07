import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(range(n, 0, -1))
flag = True

while len(queue) != 1:
    if flag:
        queue.pop()
        flag = False
    else:
        queue.insert(0, queue.pop())
        flag = True

print(queue[0])