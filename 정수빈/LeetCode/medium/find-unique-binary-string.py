# https://leetcode.com/problems/find-unique-binary-string
# 걸린시간 5분

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = int("1"*len(nums[0]), 2)
        ln = len(nums[0])
        for i in range(n+1):
            m = len(bin(i)[2:])
            binary = (ln-m)*"0"+bin(i)[2:]
            if not binary in nums:
                break
        return binary