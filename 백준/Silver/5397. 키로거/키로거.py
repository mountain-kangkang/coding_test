test_case = int(input())
result = []

for index_test_case in range(test_case):
    password = input()
    left = []
    right = []
    
    for pw in password:
        if pw == "<":
            if left:
                right.append(left.pop())
        elif pw == ">":
            if right:
                left.append(right.pop())
        elif pw == "-":
            if left:
                left.pop()
        else:
            left.append(pw)
    
    # 최종 비밀번호 생성
    sum_temp_password = "".join(left) + "".join(reversed(right))
    result.append(sum_temp_password)

for res in result:
    print(res)
