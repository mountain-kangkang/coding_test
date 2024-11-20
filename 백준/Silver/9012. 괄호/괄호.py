import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    vps = []
    for ps in input().rstrip():
        if vps == []:
            vps.append(ps)
            continue
        if vps[-1] + ps == "()":
            vps.pop()
        else:
            vps.append(ps)
    if vps:
        print("NO")
    else:
        print("YES")