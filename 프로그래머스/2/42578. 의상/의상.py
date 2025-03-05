def solution(clothes):
    clothes_dict = {}

    for cloth, category in clothes:
        if category in clothes_dict:
            clothes_dict[category].append(cloth)
        else:
            clothes_dict[category] = [cloth]

    result = 1
    for category in clothes_dict:
        result *= (len(clothes_dict[category]) + 1)    # 각 카테고리에서 의상을 선택하지 않는 경우 고려하여 + 1

    return result - 1    # 하지만 아무것도 입지 않는 경우는 없기 때문에 - 1

'''
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1

    후에 결과를 계산할 때 len() 계산하는 시간을 줄이기 위해 미리 숫자로서 value를 저장하는 방식
    프로그래머스 다른 사람 풀이에서 가져옴
'''
