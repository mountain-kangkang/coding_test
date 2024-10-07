import sys

stack = []

for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()
    if command == "pop":
        if stack:
            print(stack.pop(0))
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "front":
        if stack:
            print(stack[0])
        else:
            print(-1)
    elif command == "back":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(command[5:])