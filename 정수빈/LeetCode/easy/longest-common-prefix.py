# https://leetcode.com/problems/longest-common-prefix
# 난이도: easy
# 생각보다 오래걸렸던 문제 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        strs = sorted(strs, key=lambda x: len(x))
        first = strs[0]
        prefix = ""
        idx = 0
        while idx < len(first):
            check = True
            for str_ in strs[1:]:
                if first[idx] == str_[idx]:
                    check=True
                else:
                    check=False
                    break

            if check:
                prefix += first[idx]
            else:
                break
            idx += 1
        return prefix
        
        

