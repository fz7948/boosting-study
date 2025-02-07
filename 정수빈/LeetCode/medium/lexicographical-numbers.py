# https://leetcode.com/problems/lexicographical-numbers/description/?envType=problem-list-v2&envId=depth-first-search
# 감도 안잡혀서 그냥 답지봄 ㅠㅠ

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return result