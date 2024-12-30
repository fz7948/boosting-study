# https://leetcode.com/problems/add-binary/description/?envType=problem-list-v2&envId=simulation
# 난이도: easy
# simulation

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bit = str(bin(int(a,2) + int(b,2)))
        
        return bit[2:]