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

'''
설명
왼쪽과 오른쪽 리스트:
left 리스트는 커서 왼쪽의 문자를, right 리스트는 커서 오른쪽의 문자를 관리합니다.
이를 통해 삽입과 삭제가 O(1)로 이루어집니다.

커서 이동:
< 와 > 명령어를 통해 left와 right 리스트 간에 문자를 이동시키는 방식으로 커서를 관리합니다.

최종 비밀번호 생성:
left 리스트의 문자들을 그대로 사용하고, right 리스트는 역순으로 합쳐 최종 비밀번호를 만듭니다.'''
