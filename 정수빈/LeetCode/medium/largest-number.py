# https://leetcode.com/problems/largest-number/description/?envType=problem-list-v2&envId=greedy
# 비슷하게까지 갔지만 혼자서는 못품.. 
# 새로운 정렬방법을 알았다. 

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = sorted(list(map(str, nums)), key=lambda a: a*10, reverse=True)
        a = list(map(lambda a: a* 10, map(str, nums)))
        if nums_str[0] == "0":
            return "0"


        return "".join(nums_str)