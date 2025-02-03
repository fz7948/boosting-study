# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        i = 0
        sum_list = [0 for _ in range(n//2)]
        node = head
        while node:
            if i < n // 2:
                sum_list[i] += node.val
            else:
                sum_list[n-1-i] += node.val
            node = node.next
            i += 1
        return max(sum_list)