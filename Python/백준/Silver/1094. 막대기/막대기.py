stick = [64]
x = int(input())

while x:
    if x == sum(stick):
        break
    if x < stick[0]:
        stick[0] //= 2
        if stick[0] < x < stick[0]*2:
            stick.append(stick[0])
        continue
    if x <= sum(stick[:-1], stick[-1]//2):
        stick[-1] //= 2
        continue
    if x > sum(stick[:-1], stick[-1]//2):
        stick[-1] //= 2
        stick.append(stick[-1])
print(len(stick))