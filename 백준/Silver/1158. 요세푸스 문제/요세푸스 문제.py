n, k = map(int, input().split())

temp = []
result = []

for i in range(n):
    temp.append(i + 1)

index = -1
while True:
    if len(temp) == 0:
        break
    
    index += k
    if index >= len(temp):
        index -= (index // len(temp)) * len(temp)
    
    result.append(temp[index])
    del temp[index]
    index -= 1

print("<", end="")
for i in range(n):
    print(result[i], end="")
    if result[i] == result[n - 1]:
        break

    print(end=", ")

print(">")
