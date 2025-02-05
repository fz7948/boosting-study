# https://leetcode.com/problems/basic-calculator-ii/
# 걸린시간: 30분

from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        num = ""
        s_list = []
        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            else:
                if num and num != " ":
                    s_list.append(num)
                    num = ""
                if s[i] and s[i] != " ":
                    s_list.append(s[i])
        if num != "":
            s_list.append(num)
        s_list = deque(s_list)


        if len(s_list) == 1:
            return int(s_list[0])

        q = deque([int(s_list.popleft())])
        
        while s_list:
            n = s_list.popleft()
            if n == "*":
                next_n = int(s_list.popleft())
                q.append(int(q.pop()) * next_n)
            elif n == "/":
                next_n = int(s_list.popleft())
                q.append(int(q.pop()) // next_n)
            else:
                q.append(n)
        if len(q) == 1:
            return int(q[0])
        
        next_q = [q.popleft()]
        while q:
            n = q.popleft()
            if n == "+":
                next_n = int(q.popleft())
                next_q.append(int(next_q.pop()) + next_n)
            elif n == "-":
                next_n = int(q.popleft())
                next_q.append(int(next_q.pop()) - next_n)
            else:
                next_q.append(int(n))
        return next_q[0]
        