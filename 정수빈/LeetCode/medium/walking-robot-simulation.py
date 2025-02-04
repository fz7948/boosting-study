# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        from collections import Counter
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        d_idx = 0
        r, c = (0, 0)
        ans = 0
        obstacles = set([(x[0], x[1]) for x in obstacles])
        counter = Counter(obstacles)
        # print(counter)

        for command in commands:
            if command == -1:
                d_idx = (d_idx + 1) % 4
            elif command == -2:
                d_idx = (d_idx + 3) % 4
            else:
                dr, dc = directions[d_idx]
                for _ in range(command):
                    nr, nc = dr + r, dc + c
                    if (nc, nr) in obstacles:
                        break
                    r, c = nr, nc
                ans = max(r*r + c*c, ans)
        return ans
                


