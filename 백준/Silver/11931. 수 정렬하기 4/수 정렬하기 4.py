import sys

input = sys.stdin.readline

a = [None] * 2000001
n = int(input())
for _ in range(n):
    temp = int(input())
    if not a[temp]:
        a[temp]= 1

for i in range(1000000, -1000001, -1):
    if a[i]:
        sys.stdout.write(f'{i}\n')