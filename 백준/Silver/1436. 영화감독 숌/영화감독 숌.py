import sys

N = int(sys.stdin.readline())
temp = []
num = 666

while num:
    if '666' in str(num):
        temp.append(num)
    if N == len(temp):
        break
    num += 1

print(temp[-1])