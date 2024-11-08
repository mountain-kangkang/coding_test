import sys

input = sys.stdin.readline

num, goal = map(int, input().split())
people = [int(input()) for i in range(num)]
target = 0
cnt = 0

while target != goal:
    cnt += 1
    target = people[target]
    if cnt > num:
        cnt = -1
        break

print(cnt)