# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/editorial/?envType=study-plan-v2&envId=binary-search
# 설명: bs

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lp, rp = 0, len(nums) - 1
        ans = set()

        while lp <= rp:
            mid = (lp + rp) // 2
            middle = nums[mid]

            if middle < target:
                lp += 1
            elif middle > target:
                rp -= 1
            else:
                ilp, irp = mid, mid
                while 0 <= ilp < len(nums) and nums[ilp] == target:
                    ans.add(ilp)
                    ilp -= 1

                while 0 <= irp < len(nums) and nums[irp] == target:
                    ans.add(irp)
                    irp += 1
                print(ans)
                break
        ans = sorted(list(ans))
        if len(ans) == 1:
            e = ans[0]
            return [e, e]

        if lp == len(nums) -1 or len(ans) == 0:
            return [-1, -1]

        return [ans[0], ans[-1]]

            
