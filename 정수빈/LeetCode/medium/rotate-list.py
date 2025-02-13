# https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        prev = None
        curr = head
        count = 0
        length = 0
        while curr != None:
            prev = curr
            curr = curr.next
            length += 1
        k = k % length
        prev = None
        curr = head
        while count < k:
            while curr.next != None:
                prev = curr
                curr = curr.next
            
            if prev != None:
                prev.next = None
                curr.next = head
                head = curr
            count +=1 
        return head