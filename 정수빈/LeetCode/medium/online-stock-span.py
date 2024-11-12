# https://leetcode.com/problems/online-stock-span/?envType=study-plan-v2&envId=leetcode-75
class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.answer = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if not self.answer:
            self.stack.append((price, 0))
            self.answer.append(1)
            return self.answer[-1]
        self.answer.append(1)
        idx = len(self.answer) -1
        count = 1
        # print(self.answer, self.stack)
        check = True
        while self.stack:
            if self.stack[-1][0] > price:
                self.stack.append((price, idx))
                check = False
                break
            else:
                _, stack_idx = self.stack.pop()
                count += self.answer[stack_idx]
        if check:
            self.stack.append((price, idx))
        self.answer[idx] = count

        return self.answer[-1]

stockSpanner = StockSpanner()
# print(stockSpanner.next(100)) # return 1
# print(stockSpanner.next(80))  # return 1
# print(stockSpanner.next(60))  # return 1
# print(stockSpanner.next(70))  # return 2
# print(stockSpanner.next(60))  # return 1
# print(stockSpanner.next(75))  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# print(stockSpanner.next(85))  # return 6

# stockSpanner = StockSpanner()
print(stockSpanner.next(31)) # return 1
print(stockSpanner.next(41))  # return 2
print(stockSpanner.next(48))  # return 3
print(stockSpanner.next(59))  # return 4
print(stockSpanner.next(79))  # return 5