import sys

a = [None] * 20000001
n = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    a[i] = 1
m = int(sys.stdin.readline())
m_card = list(map(int, sys.stdin.readline().split()))
for i in m_card:
    if a[i]:
        sys.stdout.write("1 ")
    else:
        sys.stdout.write("0 ")