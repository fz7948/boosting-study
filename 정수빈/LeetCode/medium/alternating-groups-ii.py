# https://leetcode.com/problems/alternating-groups-ii
# 중요한 점은 colors 배열의 길이를 k-1만큼 늘려주는 것이다.
# 2 pointer를 사용하여 풀 수 있다.
# left와 right를 0, 1로 초기화하고, right가 colors의 길이보다 작을 때까지 반복한다.

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        length = len(colors)
        result = 0
        left = 0
        right = 1

        while right < length:
            if colors[right] == colors[right-1]:
                left = right
                right += 1
                continue
            right += 1

            if right - left < k:
                continue
            
            result += 1
            left += 1
        return result