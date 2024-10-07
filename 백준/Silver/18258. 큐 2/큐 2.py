import sys
from collections import deque

stack = deque()

for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()
    
    if command == "pop":
        if stack:
            print(stack.popleft())  # 앞에서 원소를 제거하고 반환
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if not stack else 0)
    elif command == "front":
        if stack:
            print(stack[0])  # 앞의 원소 반환
        else:
            print(-1)
    elif command == "back":
        if stack:
            print(stack[-1])  # 뒤의 원소 반환
        else:
            print(-1)
    else:
        stack.append(command[5:])  # "push x"에서 x를 추출하여 추가
