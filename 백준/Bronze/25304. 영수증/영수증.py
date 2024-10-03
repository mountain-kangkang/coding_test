total = int(input())
item = int(input())

temp = 0

for i in range(item):
    price, ea = map(int, input().split())
    temp += price * ea

if temp == total:
    print("Yes")
else:
    print("No")