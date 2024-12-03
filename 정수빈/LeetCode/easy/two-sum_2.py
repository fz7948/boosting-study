# https://leetcode.com/problems/two-sum
# 설명: 두 수의 합이 target이 되는 수를 구하는 문제입니다. 해시맵, 이전에 같은 문제를 다르게 품
# 난이도: easy, 걸린시간 7분 30초

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            n = nums[i]
            if target-n in d and i != d[target-n]:
                return (i, d[target-n])