import sys

num_list = []

for _ in range(int(sys.stdin.readline().strip())):
    num = int(sys.stdin.readline().strip())
    if num == 0 and num_list:
        num_list.pop()
    else:
        num_list.append(num)

print(sum(num_list))