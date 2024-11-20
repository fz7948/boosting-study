# https://leetcode.com/problems/rotate-array
# 설명: 배열을 회전하는 문제, 처음에 한칸씩 보내는걸로 짰다가 타임아웃남, 배열을 선언해서 해볼수도 있었지만.. 먼가 배열없이 해보고 싶어서 했는데, 좀 더 이상해진 듯 함..
# 배열의 뒷부분 k만큼 미리 저장해두고, 앞의 배열을 inplace로 바꿈 
# 난이도: medium, 시간: 19분

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def move(_nums):
            end = _nums[-k:]
            for i in range(len(_nums)-k):
                t = len(_nums)- k - i -1
                _nums[t+k] = _nums[t]
            _nums[:k] = end

        if k == 0 or k % len(nums) == 0:
            return nums 
        
        k = k % len(nums) 

        if len(nums) <= 1:
            return nums
        move(nums)
