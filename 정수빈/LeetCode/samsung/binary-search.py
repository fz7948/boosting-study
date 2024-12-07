# https://leetcode.com/problems/binary-search/?envType=company&envId=samsung&favoriteSlug=samsung-all
# 난이도: easy
# 해결 x
# 설명: 바이너리 서치, 엄청 쉬운 건데 rp, lp 세팅을 제대로 못함..

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) -1
        while lp <= rp:
            mid = (lp + rp) // 2
            middle = nums[mid]
            if middle > target:
                rp = mid - 1
            elif middle == target:
                return mid
            else:
                lp = mid + 1
        return -1
            