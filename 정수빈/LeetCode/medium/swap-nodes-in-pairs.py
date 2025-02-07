# https://leetcode.com/problems/swap-nodes-in-pairs/
# 걸린시간: 20분

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        node_list = []
        while node:
            node_list.append(node)
            node = node.next
        
        for i in range(len(node_list)):
            if i % 2 == 0 and i+1 < len(node_list):
                tmp = node_list[i]
                node_list[i] = node_list[i+1]
                node_list[i+1] = tmp

        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
            node_list[i+1].next = None

        return node_list[0] if node_list else None