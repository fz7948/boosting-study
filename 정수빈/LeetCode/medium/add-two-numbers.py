# https://leetcode.com/problems/add-two-numbers/
# 설명: 링크드리스트의 값을 합해서 다시 링크드리스트로 반환하는 문제입니다. while을 사용해서 링크드리스트의 값을 
# 전부 가져온 다음, 합하고 링크드리스트를 만들었습니다. 
# 난이도: medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node1 = l1
        node1_num = str(node1.val)
        node2 = l2
        node2_num = str(node2.val)
        while node1.next:
            node1_num = node1_num + str(node1.next.val)
            
            node1 = node1.next

        while node2.next:
            node2_num = node2_num + str(node2.next.val)
            
            node2 = node2.next

        node_num = str(int(node1_num[::-1]) + int(node2_num[::-1]))
        idx = len(node_num)-1
        node = ListNode(int(node_num[idx]))
        root = node
        while idx > 0:
            idx -= 1
            node.next = ListNode(int(node_num[idx]))
            node = node.next
            
        return root
        