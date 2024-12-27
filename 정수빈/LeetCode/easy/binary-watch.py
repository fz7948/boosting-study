# https://leetcode.com/problems/binary-watch/?envType=problem-list-v2&envId=backtracking
# 설명: bk

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour = [8, 4, 2, 1]
        hour_active = [False for _ in range(4)]
        minute = [32, 16, 8, 4, 2, 1]
        minute_active = [False for _ in range(6)]
        time_set = set()

        def get_time():
            hour_num = 0
            min_num = 0
            for i in range(4):
                if hour_active[i]:
                    hour_num += hour[i]
            for i in range(6):
                if minute_active[i]:
                    min_num += minute[i]

            if hour_num > 11 or min_num > 59:
                return 

            return f"{hour_num}:{min_num:02d}"

        def bk(hour_idx, min_idx, count):
            if count == turnedOn:
                if get_time():
                    time_set.add(get_time())
                return 
            if hour_idx < 4 and count < turnedOn:
                bk(hour_idx+1, min_idx, count)
                hour_active[hour_idx] = True
                bk(hour_idx+1, min_idx, count+1)
                hour_active[hour_idx] = False
            if min_idx < 6 and count < turnedOn:
                bk(hour_idx, min_idx+1, count)
                minute_active[min_idx] = True
                bk(hour_idx, min_idx+1, count+1)
                minute_active[min_idx] = False
        bk(0, 0, 0)

        return sorted(list(time_set))