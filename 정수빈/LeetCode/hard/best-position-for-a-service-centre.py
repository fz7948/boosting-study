# https://leetcode.com/problems/best-position-for-a-service-centre/
# 설명을 보고 이해하려고 노력했지만, 이해가 잘 되지 않아서 다른 사람의 코드를 참고했다.

from typing import List
from math import sqrt

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # Euclidean distance function
        def distance(x, y):
            return sum(sqrt((x - px) ** 2 + (y - py) ** 2) for px, py in positions)
        
        # Initialize centroid as the starting point
        x = sum(px for px, _ in positions) / len(positions)
        y = sum(py for _, py in positions) / len(positions)
        
        # Start with a larger change (step size)
        step = 50
        epsilon = 1e-6  # Accuracy within 1e-6
        min_dist = distance(x, y)
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while step > epsilon:
            improved = False
            for dx, dy in directions:
                nx, ny = x + step * dx, y + step * dy
                new_dist = distance(nx, ny)
                if new_dist < min_dist:
                    min_dist = new_dist
                    x, y = nx, ny
                    improved = True
                    break  # Move to the new position immediately
            
            if not improved:
                step /= 2  # Reduce the step size when no improvement is found
        
        return min_dist
