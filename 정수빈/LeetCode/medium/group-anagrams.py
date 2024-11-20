# https://leetcode.com/problems/group-anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dc = {}
        for s in strs:
            key = tuple(sorted(list(s)))
            if not key in dc:
                dc[key] = [s]
            else:
                dc[key].append(s)
        return list(dc.values())

print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])