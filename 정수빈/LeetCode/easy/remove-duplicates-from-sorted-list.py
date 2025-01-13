# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            if prev and prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
     
        return head