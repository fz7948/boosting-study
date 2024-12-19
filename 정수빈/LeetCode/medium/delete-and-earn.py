# https://leetcode.com/problems/delete-and-earn/?envType=study-plan-v2&envId=dynamic-programming
# 설명: dp
# 난이도: medium 

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter

        counter_nums = Counter(nums)
        counter_nums_key = sorted(counter_nums.keys())
        ans = [0 for _ in range(len(counter_nums_key))]
        
        for i in range(len(counter_nums_key)):
            key = counter_nums_key[i]
            if i == 0:
                ans[0] = counter_nums[key] * key
                continue
            
            if key - 1 == counter_nums_key[i-1]:
                ans[i] = max(ans[i-1], ans[i-2] + counter_nums[key] * key)
            else:
                ans[i] = max(ans[i-1], ans[i-1] + counter_nums[key] * key)
        # print(ans)
        return ans[-1]
            
        