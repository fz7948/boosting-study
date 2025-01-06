# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75
# 유형: Sliding Window
# 시간: 10분
# 난이도: medium

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lp = 0
        rp = 0
        max_len = 0
        while rp < len(nums): 
            if nums[rp] == 1:
                rp += 1
            elif nums[rp] == 0 and k > 0:
                rp +=1
                k -= 1
            elif nums[rp] == 0 and k == 0:
                for i in range(lp, rp+1):
                    if nums[i] == 0:
                        lp = i+1
                        rp += 1
                        break
            max_len = max(max_len, rp - lp)
        return max_len
            