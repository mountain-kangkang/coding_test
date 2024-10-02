year = int(input())

if year % 4 != 0:
    print(0)
else:
    if year % 100 == 0 and year % 400 != 0:
        print(0)
    else:
        print(1)