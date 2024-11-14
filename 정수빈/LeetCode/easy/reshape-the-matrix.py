class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat

        ans = []
        one_d = []
        for i in range(len(mat)):
            one_d.extend(mat[i])

        idx = 0
        
        for i in range(r):
            ans.append([])
            for _ in range(c):
                ans[i].append(one_d[idx])
                idx +=1

        return ans

# print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4), [[1,2,3,4]])
print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4), [[1,2],[3,4]])