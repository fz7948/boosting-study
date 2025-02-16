# https://leetcode.com/problems/decode-ways/
# 메모리 아웃이 나서 결국 답지를 보긴했지만 아래와 비슷한 흐름으로 풀었습니다. @lru_cache(maxsize=None) 이걸 쓰면 자동으로 함수를 캐싱해준다네여
# 신기..

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def recursiveWithMemo(index) -> int:
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index == len(s) - 1:
                return 1

            answer = recursiveWithMemo(index + 1)
            if int(s[index : index + 2]) <= 26:
                answer += recursiveWithMemo(index + 2)

            return answer

        return recursiveWithMemo(0)