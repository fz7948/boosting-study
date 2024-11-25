# https://leetcode.com/problems/generate-parentheses
# 난이도: medium 
# 설명: backtracking
# 시간: 13분 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        def valid_parentheses(comb):
            t = 0
            for s in comb:
                if s == "(":
                    t +=1
                else:
                    t -= 1
                if t < 0:
                    return False
            return t == 0

        def bk(comb):
            if len(comb) == n*2 and valid_parentheses(comb):
                ans.add("".join(comb))
                return
            elif len(comb) >= n*2:
                return 

            bk(comb + ["("])
            bk(comb + [")"])
        
        bk(["("])
        return list(ans)