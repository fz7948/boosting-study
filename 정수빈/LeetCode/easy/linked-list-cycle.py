# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = set()
        node = head
        while node:
            if node.next == None:
                return False
            elif node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
            
            
