# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = collections.deque(path.split("/"))
        # print(path)
        s = [path.popleft()]
        while path:
            p = path.popleft()
            if p == "":
                pass
            elif p == "..":
                if s:
                    s.pop()
            elif p == ".":
                pass
            else:
                s.append(p)
            # print(s)
        path = ""
        for c in s:
            if c != "":
                path += "/"+c
        return path if len(path) > 0 else "/"
