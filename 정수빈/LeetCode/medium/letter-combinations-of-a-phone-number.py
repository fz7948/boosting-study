# https://leetcode.com/problems/letter-combinations-of-a-phone-number
# 설명: 백트레킹 문제인데 전혀 백트레킹처럼 안풀었다는... 숫자를 영문으로 변경하고 그에 맞는 모든 조합을 찾는 문제
# 난이도: medium
# 시간: 16분

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz")
        }
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(alpha[digits])

        elif len(digits) == 2:
            ans = []
            for d1 in alpha[digits[0]]:
                for d2 in  alpha[digits[1]]:
                    c = d1+d2
                    ans.append(c)
            return list(set(ans))
        elif len(digits) == 3:
            ans = []
            for d1 in alpha[digits[0]]:
                for d2 in  alpha[digits[1]]:
                    for d3 in  alpha[digits[2]]:
                        c = d1+d2+d3
                        ans.append(c)
            return list(set(ans))
        elif len(digits) == 4:
            ans = []
            for d1 in alpha[digits[0]]:
                for d2 in  alpha[digits[1]]:
                    for d3 in  alpha[digits[2]]:
                        for d4 in  alpha[digits[3]]:
                            c = d1+d2+d3+d4
                            ans.append(c)
            return list(set(ans))        

