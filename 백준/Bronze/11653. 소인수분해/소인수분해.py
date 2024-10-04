n = int(input())

while True:
    if n == 1:
        break
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            if n == i:
                n = 1
                break
            n //= i
            break