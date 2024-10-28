def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0

    for i in range(len(answers)):
        if answers[i] == a[i%len(a) if len(answers) > len(a) else i]:
            a_cnt += 1
        if answers[i] == b[i%len(b) if len(answers) > len(b) else i]:
            b_cnt += 1
        if answers[i] == c[i%len(c) if len(answers) > len(c) else i]:
            c_cnt += 1

    answer = []
    max_ = max(a_cnt, b_cnt, c_cnt)
    if max_ == a_cnt:
        answer.append(1)
    if max_ == b_cnt:
        answer.append(2)
    if max_ == c_cnt:
        answer.append(3)
    return answer