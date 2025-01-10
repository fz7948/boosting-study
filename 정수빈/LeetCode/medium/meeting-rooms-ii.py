# https://leetcode.com/problems/meeting-rooms-ii/description/?envType=problem-list-v2&envId=greedy
# 이것도 답보고 함.. 흑흑
# 유형: two pointer, greedy 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([start for (start, _) in intervals])
        ends = sorted([end for (_, end) in intervals])
        count = 0
        sidx = 0
        eidx = 0
        max_count = 0
        while sidx < len(intervals):
            if starts[sidx] < ends[eidx]:
                count += 1
                sidx += 1
                max_count = max(count, max_count)
            else:
                count -= 1
                eidx += 1    
        return max_count