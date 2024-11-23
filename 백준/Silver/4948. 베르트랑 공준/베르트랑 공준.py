import sys

input = sys.stdin.readline

l = [True] * ((123456 * 2)+1)
limit = 123456 * 2

l[0] =  l[1] = False 

for i in range(2, int(limit**0.5)+1):
    if l[i]:
        for j in range(i*i, limit+1, i):
            l[j] = False

while True:
    n = int(input())
    if n < 1 or n > 123456:
        break

    print(sum(1 for i in range(n+1, n*2+1) if l[i]))