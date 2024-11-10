# https://leetcode.com/problems/k-diff-pairs-in-an-array/
# 설명: 요소 2개를 선택했을 때 두 값의 차이가 k인 숫자쌍을 찾는 것
# 리스트를 정렬 후 왼쪽 포인트, 오른쪽 포인트를 생성하여 숫자의 차이가 K보다 작으면 오른쪽 포인트를 오른쪽으로 옮김

class Solution(object):
    def findPairs(self, nums, k):
        nums.sort()
        pairs = {}
        lp = 0
        rp = 1
        answer = 0
        while rp < len(nums):
            if nums[rp] - nums[lp] == k and rp != lp:
                if not (nums[lp], nums[rp]) in pairs:
                    answer += 1
                    pairs[(nums[lp], nums[rp])] = 1
                rp += 1
            elif nums[rp] - nums[lp] < k:
                rp += 1
            elif lp >= rp:
                rp += 1
            else:
                lp += 1

        return answer

        