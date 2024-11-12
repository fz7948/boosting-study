# https://leetcode.com/problems/string-compression

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        cur = chars[0]
        idx = 1
        while idx < len(chars):
            if cur == chars[idx]:
                chars.pop(idx)
                count += 1
            else:
                if count == 1:
                    pass
                else:
                    n = list(str(count))
                    for m in range(len(n)):
                        chars.insert(idx, n[m])
                        idx += 1
                cur = chars[idx]
                count = 1
                idx += 1
        if count > 1:
            n = list(str(count))
            for m in range(len(n)):
                chars.append(n[m])
        return len(chars)
        