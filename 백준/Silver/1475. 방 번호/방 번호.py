room = list(input())

set_count = 0
while room:
    for i in range(10):
        if i == 6 or i == 9:
            if i == 6 and room.count('6') == 0 and room.count('9'):
                room.remove('9')
                continue
            if i == 9 and room.count('9') == 0 and room.count('6'):
                room.remove('6')
                continue
        if room.count(str(i)):
            room.remove(str(i))
    set_count += 1
    if room == []:
        break
print(set_count)