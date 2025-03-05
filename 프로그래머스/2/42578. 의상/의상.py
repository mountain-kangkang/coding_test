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
