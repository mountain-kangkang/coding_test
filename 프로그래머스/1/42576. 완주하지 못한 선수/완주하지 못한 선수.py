# def solution(participant, completion): 효율성 통과 실패
#     p_dict = {}
#     c_dict = {}
#     for p in participant:
#         p_dict[p] = participant.count(p)
#     for c in completion:
#         if c not in c_dict:
#             c_dict[c] = completion.count(c)
#     for c in c_dict:
#         p_dict[c] -= c_dict[c]
#     for key, val in p_dict.items():
#         if val:
#             return key

def solution(participant, completion):
    part = {}

    for p in participant:
        if p in part : part[p] += 1
        else : part[p] = 1

    for c in completion:
        part[c] -= 1

    return ''.join([name for name in part if part[name] == 1])