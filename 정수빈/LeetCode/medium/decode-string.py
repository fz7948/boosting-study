# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75
# 여러번 시도해보다가 결국 풀었던 문제! 

from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        s = deque(list(s))
        q = []

        while s:
            c = s.popleft()
            if c == "]":
                n = q.pop()
                word = ""
                while n != "[":
                    word = n + word
                    n = q.pop()

                count = ""
                while q and q[-1].isdigit():
                    count = q.pop() + count
                q.append(word * int(count))
            else:
                q.append(c)

        return "".join(q)
