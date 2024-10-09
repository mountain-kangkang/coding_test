import sys

N = int(sys.stdin.readline())

delivery = []

for i in range((N//5)+1):
    three = (N - (5 * i)) // 3
    if N - ((5 * i) + (three * 3)) == 0:
        delivery.append(i + three)

if delivery:
    print(min(delivery))
else:
    print(-1)