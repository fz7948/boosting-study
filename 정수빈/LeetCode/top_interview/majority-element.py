# https://leetcode.com/problems/majority-element
# 설명: 배열안에 숫자가 가장 많이 있는 수를 구하는 문제입니다. 추가 문제로 O(1)을 할 수 있는지 물어봤는데, 
# 이건 O(n)이네요 
# 난이도: easy


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        return Counter(nums).most_common()[0][0]
        
# 이게 solution에서 본 O(1)인데 신기하게 잘해놨네여 ㅋㅋ

# class Solution(object):
#     def majorityElement(self, nums):
#         count=0
#         number=None
#         for num in nums:
#             if count==0:
#                 number=num
#             if num==number:
#                 count+=1
#             else:
#                 count-=1
#         return number
        
        