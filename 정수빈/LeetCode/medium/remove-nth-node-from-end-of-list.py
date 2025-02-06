# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 걸린시간: 13분

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        node_list = []
        while node:
            node_list.append(node)
            node = node.next
        m = len(node_list)
        if 0 <= m-n-1 < m and m-n+1 < m:
            node_list[m-n-1].next = node_list[m-n+1]
        elif 0 <= m-n-1 < m and m-n+1 >= m - 1:
            node_list[m-n-1].next = None
        elif m-n-1 < 0  and m-n+1 < m:
            head = node_list[m-n+1]
        else:
            head = None
        return head