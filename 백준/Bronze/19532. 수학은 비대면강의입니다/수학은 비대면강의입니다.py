import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
x, y = 0, 0
flag = False

for temp_x in range(-999, 1000):
    for temp_y in range(-999, 1000):
        if (a * temp_x) + (b * temp_y) == c:
            if (d * temp_x) + (e * temp_y) == f:
                x = temp_x
                y = temp_y
                flag = True
                break
    if flag:
        break

print(x, y)