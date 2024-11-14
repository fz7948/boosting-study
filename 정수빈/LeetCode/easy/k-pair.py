class Solution(object):
    def findPairs(self, nums, k):
        from collections import Counter
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        if k == 0:
            for k, v in Counter(nums).items():
                if v > 1:
                    count += 1
            return count

        nums = list(set(nums))
        nums.sort()
        # print(nums)

        ans_set = set()

        for i in range(len(nums)):
            # print("out",i, min(i+k+2, len(nums)))
            for j in range(i+1, min(i+k+1, len(nums))):
                # print("in",i, j, (nums[i], nums[j]))
                if not (nums[i], nums[j]) in ans_set and k == abs(nums[i] - nums[j]):
                    ans_set.add((nums[i], nums[j]))
                    count += 1
        # print("---")
        return count
print(Solution().findPairs([1,3,1,5,4], 0), 1)
print(Solution().findPairs([1,2,4,4,3,3,0,9,2,3], 3), 2)