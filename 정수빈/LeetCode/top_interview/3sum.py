# https://leetcode.com/problems/3sum/description
# 설명: 3sum 을 구합니다. 아래의 알고리즘으로 하면 timeout이 납니다. 아래는 해시테이블로 푼 문제입니다. 
# https://www.youtube.com/watch?v=jzZsG8n2R9A 하나를 고정해놓고 two pointer로 찾음 (2 sum문제로 변형됨)
# 난이도: medium 시간: 20분


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        sum_dic = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                key = nums[i] + nums[j]
                if not key in sum_dic:
                    sum_dic[key] = []
                sum_dic[key].append([i, j])

        for k in range(len(nums)):
            if -nums[k] in sum_dic:
                for t1, t2 in sum_dic[-nums[k]]:
                    if t1 != k and t2 != k: 
                        a = [nums[t1], nums[t2], nums[k]]
                        a.sort()
                        ans.add(tuple(a))
        
        return [list(x) for x in ans]


