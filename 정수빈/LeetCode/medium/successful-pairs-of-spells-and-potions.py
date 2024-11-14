class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        ans = []
        for sp in spells:
            count = 0
            for i, p in enumerate(potions):
                if sp * p >= success:
                    count += len(potions[i:])
                    ans.append(count)
                    break
            if count == 0:
                ans.append(0)
        
        return ans

print(Solution().successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7), [4,0,3])