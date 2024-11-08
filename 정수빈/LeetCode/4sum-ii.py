# https://leetcode.com/problems/4sum-ii/
# 설명: 4개의 배열이 있고, 배열 안의 요소의 합이 0인 것을 찾아야 함

from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        answer = 0
        d = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                d[n1+n2] += 1

        for n3 in nums3: 
            for n4 in nums4:
                answer += d[-(n3+n4)]
                
        return answer