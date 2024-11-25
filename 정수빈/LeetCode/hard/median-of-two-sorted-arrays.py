# https://leetcode.com/problems/median-of-two-sorted-arrays/
# 난이도: hard
# 시간: 40분
# 설명: 두 정렬된 리스트에서 메디안을 구하는 문제. 2 포인터를 이용하여 해결

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsLen = len(nums1) + len(nums2)
        ans = -1
        if nums1 and nums2: 
            ans = min(nums1[0], nums2[0])
        elif nums1:
            ans = nums1[0]
        elif nums2:
            ans = nums2[0]
        else:
            return 0.0
        endIdx = numsLen  // 2
        p1 = 0
        p2 = 0
        prev = -1
        while p1 + p2 <= endIdx:
            prev = ans
            # print(p1, p2, ans, endIdx)
            if p1 < len(nums1) and p2 < len(nums2) and nums1[p1] >= nums2[p2]:
                ans = nums2[p2]
                p2 += 1
            elif p1 < len(nums1) and p2 < len(nums2) and nums1[p1] < nums2[p2]:
                ans = nums1[p1]
                p1 += 1
            elif p1 < len(nums1):
                ans = nums1[p1]
                p1 +=1
            elif p2 < len(nums2):
                ans = nums2[p2]
                p2 += 1
            else:
                if len(nums1) < len(nums2):
                    p2 +=1
                else: p1 +=1
        if numsLen % 2:
            return ans
        else:
            return (ans + prev) / 2.0



