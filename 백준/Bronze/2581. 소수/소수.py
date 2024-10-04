m = int(input())
n = int(input())
arr = []

for i in range(m, n + 1):
    temp = []
    for j in range(1, i + 1):
        if i % j == 0:
            temp.append(j)
    if len(temp) == 2:
        arr.append(i)
if arr == []:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])