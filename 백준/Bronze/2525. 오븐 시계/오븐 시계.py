a, b = map(int, input().split())
c = int(input())

b += c

if b >= 60:
    temp = b // 60
    b -= (60 * temp)
    a += temp
    if a >= 24:
        a -= 24
        
print(f"{a} {b}")