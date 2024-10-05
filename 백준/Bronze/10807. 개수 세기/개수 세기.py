n = int(input())
num_list = list(map(int, input().split()))

if n != len(num_list):
    print("error!")
else:
    find = int(input())

count = 0
for num in num_list:
    if num == find:
        count += 1
print(count)