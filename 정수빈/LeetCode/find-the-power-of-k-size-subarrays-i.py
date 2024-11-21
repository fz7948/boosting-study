# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i
# 설명: 연속된 숫자 + 정렬된 숫자 크기 k인 subarray를 구하는 문제입니다. 
# 전체적인 loop을 해주고 작게 k loop을 해주었습니다. 
# 난이도: medium
# 시간: 7분

class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums
        ans = []
        for i in range(len(nums)-k+1):
            count = 1
            for j in range(1, k):
                if nums[i+j-1] < nums[i+j] and nums[i+j] - nums[i+j-1] == 1:
                    count += 1
                    if count == k:
                        ans.append(nums[i+j])
                else:
                    ans.append(-1)
                    break
        return ans
