n, k = map(int, input().split())
temp = []

for i in range(1, n + 1):
    if n % i == 0:
        temp.append(i)

try:
    print(temp[k - 1])
except IndexError:
    print(0)