# https://leetcode.com/problems/number-of-recent-calls

class RecentCounter(object):

    def __init__(self):
        self.range = []
        self.requests = []
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.requests.append(t)
        self.range = [t - 3000, t]
        while self.requests[0] < self.range[0]:
            self.requests.pop(0)
        return len(self.requests)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)