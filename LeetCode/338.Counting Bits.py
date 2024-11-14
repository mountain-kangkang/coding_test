class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            # # i 를 2진수로 표현하고 거기서 숫자 1의 개수를 해아려 반환해야함 
            # jinsu = 2
            # temp = []
            # while True:
            #     if i == 0:
            #         result.append(0)
            #         break
            #     elif (i - jinsu) > jinsu:
            #         jinsu * 2
            #         continue
            #     else:
            #         temp.append(1)
            #         i -= jinsu
            #         jinsu //= 2
            #     if i <= 0:
            #         break
            # result.append(sum(temp))
            result.append(bin(i).count('1'))
        return result

# 문제 링크
# https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75
# Dynamic Programming, Bit Manipulation
