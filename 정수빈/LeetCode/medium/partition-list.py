# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        prev = None
        curr = head
        if not head:
            return head
        small_list = []
        while curr != None:
            curr_next = curr.next
            if curr.val >= x:
                curr.next = None
                small_list.append(curr)
                curr = curr_next
                if prev == None:
                    head = curr
                else:
                    prev.next = curr_next
            else:
                prev = curr
                curr = curr_next
        tail = prev
        tail_head = tail
        if tail == None:
            tail = small_list.pop(0)
            tail_head = tail
        for elem in small_list:
            tail.next = elem
            tail = elem
        if not head:
            return tail_head
        return head
            
    