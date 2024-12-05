# https://leetcode.com/problems/reverse-integer/
# 빈도수
# 설명: str로 숫자를 뒤집었지만, int를 사용하는 게 정배인거 같습니다. 

class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31-1:
            return 0
        if x >= 0:
            ret = int(str(x)[::-1])
            if ret > 2**31-1:
                return 0
            else:
                return ret
        else:
            ret = -int(str(x)[1:][::-1])
            if ret < -2**31-1:
                return 0
            else:
                return ret