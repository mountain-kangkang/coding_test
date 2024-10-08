import sys

N = int(sys.stdin.readline().strip())

M = []

for i in range(1, N):
    add_sum = i
    temp = str(add_sum)
    for j in temp:
        add_sum += int(j)

    if add_sum == N:
        M.append(i)

if M:
    print(min(M))
else:
    print(0)