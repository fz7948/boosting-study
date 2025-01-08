# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# 시간초과 떠서 답봄 
# greedy solution에 대해 공부해야할 듯 

class Solution:

    def minimumOperations(self, nums) -> int:
        lp, rp = 0, len(nums)-1
        ans = 0
        while lp < rp:
            if nums[lp] == nums[rp]:
                lp += 1
                rp -= 1
            else:
                if nums[lp] + nums[lp + 1] < nums[rp] + nums[rp - 1]:
                    nums[lp + 1] += nums[lp]
                    lp += 1
                else:
                    nums[rp -1] += nums[rp]
                    rp -= 1
                ans += 1

        # print(n, nums)
        return ans

# print(Solution().minimumOperations([90330,16730,7898,110,104,641,1,217318,229335,47379,2722,169825,446667,502479,646991,477905,470800,302249,931779,931779,302249,470800,477905,646991,502479,446667,169825,497711,115814]))
print(Solution().minimumOperations([1,2,3,4]))