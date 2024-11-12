# https://leetcode.com/problems/product-of-array-except-self/
# 설명: 배열안의 요소를 자기 자신빼고 전부 곱한 값을 구하는 문제
# 0의 갯수가 2개 이상이 되면 곱한 값이 전부 0이 될 것이고
# 0의 갯수가 1개인 경우 자기자신이 0인경우 배열 전체 곱을 정답으로 넣으면 된다. 

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rot = 1
        zeros_count = 0
        zero_index = -1
        for idx, n in enumerate(nums):
            if n == 0:
                zeros_count += 1
                zero_index = idx
            else:
                rot *= n
        if zeros_count > 1:
            return [0 for _ in range(len(nums))]
    
        t = []
        for idx, n in enumerate(nums):
            if zeros_count == 0 and n != 0:
                t.append(rot/n)
            elif zeros_count == 1 and zero_index == idx:
                t.append(rot)
            elif zeros_count == 1 and zero_index != idx:
                t.append(0)
        return t
        