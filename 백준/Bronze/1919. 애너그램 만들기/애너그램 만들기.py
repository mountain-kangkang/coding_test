a = input()
b = input()
cnt = 0
temp = []

for i in a:
    if i in temp:
        continue
    if a.count(i) - b.count(i) == 0:
        temp.append(i)
        continue
    elif a.count(i) - b.count(i) > 0:
        cnt = cnt + (a.count(i) - b.count(i))
        temp.append(i)
for i in b:
    if i in temp:
        continue
    if b.count(i) - a.count(i) == 0:
        temp.append(i)
        continue
    elif b.count(i) - a.count(i) > 0:
        cnt = cnt + (b.count(i) - a.count(i))
        temp.append(i)
print(cnt)