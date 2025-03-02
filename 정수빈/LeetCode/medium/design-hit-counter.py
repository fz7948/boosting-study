# https://leetcode.com/problems/design-hit-counter/

class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        start = timestamp - 300
        end = timestamp
        count = 0
        for i in range(len(self.hits)):
            if start < self.hits[i] <= end:
                count += 1
        return count