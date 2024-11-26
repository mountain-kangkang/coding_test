import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
meeting = sorted([list(map(int, input().split())) for _ in range(n)])

meeting_room = [meeting[0]]
for i in range(1, n):
    if meeting_room[-1][1] <= meeting[i][0]:
        meeting_room.append(meeting[i])
    elif meeting_room[-1][1] > meeting[i][1]:
        meeting_room[-1] = meeting[i]
print(str(len(meeting_room))+"\n")