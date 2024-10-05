n = int(input())
num_list = list(map(int, input().split()))

if n != len(num_list):
    print("error!")
else:
    res = int(input())
    
    count = 0
    num_set = set()  # 빠른 검색을 위한 집합 사용

    for num in num_list:
        target = res - num
        if target in num_set:
            count += 1
        num_set.add(num)

    print(count)
