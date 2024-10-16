import sys
from collections import deque

def good_word(dq:deque, flag:int) -> int:
    cal_que = deque()
    cal_flag = 0

    while dq:
        cal_que.append(dq.pop())

        if len(cal_que) == 1:
            continue
        elif len(cal_que) >= 2 and cal_que[0] == cal_que[1]:
            cal_que.pop()
            cal_que.pop()
        else:
            dq.appendleft(cal_que.popleft())
        if len(dq) >= 2 and dq[0] == dq[1]:
            dq.popleft()
            dq.popleft()
        cal_flag += 1
        
        if dq == deque() and cal_que == deque():
            return 1
        if cal_flag == flag:
            return 0

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    word = deque(sys.stdin.readline().strip())
    flag = len(word)
    if len(word) % 2:
        continue
    cnt += good_word(word, flag)

print(cnt)