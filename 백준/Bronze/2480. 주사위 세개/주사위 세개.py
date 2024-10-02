a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c or b == c:
    if a == b or a == c:
        print(1000 + a * 100)
    else:
        print(1000 + c * 100)
else:
    big = 0
    if a > b:
        big = a
    else:
        big = b
    if c > big:
        big = c
    print(big * 100)