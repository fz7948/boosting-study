class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        answer = []
        for i in range(len(matrix[0])):
            answer.append([])
            for _ in range(len(matrix)):
                answer[i].append(None)
        # print(answer)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                answer[x][y] = matrix[y][x]
        # print("---")
        return answer

print(Solution().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]), [[1,4,7],[2,5,8],[3,6,9]])
# print(Solution().transpose(matrix = [[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]])