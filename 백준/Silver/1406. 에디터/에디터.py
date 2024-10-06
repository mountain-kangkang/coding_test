import sys

left= list(sys.stdin.readline().strip())
right = []

for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip()
    if command == "L" and left:
        right.append(left.pop())
    if command == "D" and right:
        left.append(right.pop())
    if command == "B" and left:
        left.pop()
    if command[0] == "P":
        left.append(command[2])

print(''.join(left + right[::-1]))