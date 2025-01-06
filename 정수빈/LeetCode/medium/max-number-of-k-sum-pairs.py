# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
# 유형: Two Pointers
# 시간: 10분
# 난이도: medium

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        lp = 0
        rp = len(nums)-1
        count = 0
        while lp < rp:
            # print(lp, rp, nums, count)
            total = nums[lp] + nums[rp]
            if total == k:
                nums.pop(lp)
                rp -= 1
                nums.pop(rp)
                rp -= 1
                count += 1
            elif total < k:
                lp += 1
            elif total > k:
                rp -= 1

        return count
        