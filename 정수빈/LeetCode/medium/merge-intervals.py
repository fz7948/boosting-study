# https://leetcode.com/problems/merge-intervals
# 난이도: medium
# 시간: 34분
# 설명: 입력값으로 간격이 주어지고 겹치는 간격을 merge하면 되는 문제, 
# 생각보다 오래걸렸는데, 다른 사람 코드를 보니까 상당히 쉽더라구요 ㅋㅋㅋ 10줄이내로 끝내는 그들.. 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = [list(x) for x in set(tuple(x) for x in intervals)]
        intervals = sorted(list(intervals), key=lambda x: x[0])
        ans = []
        for i in range(len(intervals)):
            merge = intervals[i]
            if ans and ans[-1][0] <= merge[0] and ans[-1][1] >= merge[1]:
                continue
            for j in range(i+1, len(intervals)):
                if intervals[j][0] <= merge[1] <= intervals[j][1]:
                    merge = [min(merge[0], intervals[j][0]), intervals[j][1]]
                elif intervals[j][1] <= merge[1]:
                    merge = [min(merge[0], intervals[j][0]), merge[1]]
                else:
                    # print(4, intervals[i], intervals[j])
                    pass
            ans.append(merge)
        return ans