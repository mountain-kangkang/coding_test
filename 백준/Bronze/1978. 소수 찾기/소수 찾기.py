n = int(input())
count = 0
num = []

num = list(map(int, input().split()))

if n == len(num):
    for i in range(n):
        temp = []
        for j in range(1, num[i]+1):
            if num[i] % j == 0:
                temp.append(j)
        if len(temp) == 2:
            count += 1

    print(count)