def solution(clothes):
    clothes_dict = {}

    for cloth, category in clothes:
        if category in clothes_dict:
            clothes_dict[category].append(cloth)
        else:
            clothes_dict[category] = [cloth]

    result = 1
    for category in clothes_dict:
        result *= (len(clothes_dict[category]) + 1)

    return result - 1