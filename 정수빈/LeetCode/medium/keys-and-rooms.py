# https://leetcode.com/problems/keys-and-rooms
# 설명: 모든 방을 순회하는 문제입니다. 모든 방을 순회할 수 있으면 true 없으면 false
# stack을 이용해 dfs를 풀었습니다. 

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        stack = []
        stack.extend(rooms[0])
        visited = set()
        visited.add(0)

        while stack:
            idx = stack.pop(0)
            visited.add(idx)
            
            for r in rooms[idx]:
                if not r in visited:
                    stack.append(r)

        return len(visited) == len(rooms)
        