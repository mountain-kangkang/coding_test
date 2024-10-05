n = int(input())
temp = []
for i in range(n):
    temp.append(list(input().split()))

for i in temp:
    possible = 0
    for j in i[0]:
        if i[0].count(j) == i[1].count(j):
            possible += 1
    if possible == len(i[0]):
        print("Possible")
    else:
        print("Impossible")