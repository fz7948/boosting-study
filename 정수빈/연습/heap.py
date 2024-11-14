import heapq

class MiddleElementFinder:
    def __init__(self):
        self.heaps = [], []

    def add_num(self, num: int) -> None:
        small, large = self.heaps
        
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(small) > len(large):
            heapq.heappush(large, -heapq.heappop(small))
        print(small, large)
        

    def middle_element(self) -> int:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # We subtract `small[0]` from `large[0]`, because `small` consists of negative values
        return float((large[0] - small[0]) / 2.0)

# Let's test the code
estimate_finder = MiddleElementFinder()
estimate_finder.add_num(5)
estimate_finder.add_num(10)
estimate_finder.add_num(3)
estimate_finder.add_num(1)
estimate_finder.add_num(7)

# print(estimate_finder.middle_element()) # Expected output: 5