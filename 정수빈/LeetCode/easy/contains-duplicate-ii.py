# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = {}
        for i in range(len(nums)):
            if not nums[i] in dic:
                dic[nums[i]] = []
            dic[nums[i]].append(i)
        
        for _, v in dic.items():
            if len(v) > 1:
                for i in range(1, min(len(v), k+2)):
                    if abs(v[i] - v[i-1]) <= k:
                        return True
        return False