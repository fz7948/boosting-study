# https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            num = i
            binary = ""
            while num > 0:
                binary += str(num % 2)
                num = num // 2
            # print(binary)
            ans.append(binary.count("1"))
        return ans
