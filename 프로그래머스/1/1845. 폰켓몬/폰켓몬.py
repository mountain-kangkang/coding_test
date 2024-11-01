def solution(nums):
    phone_ketmon = [None] * 200001
    cnt = 0
    for i in nums:
        if not phone_ketmon[i]:
            phone_ketmon[i] = 1
            cnt += 1
    
    if cnt <= (len(nums) // 2):
        return cnt
    else:
        return len(nums) // 2