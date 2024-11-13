class ReverseLinkedList {

    /*
        206. Reverse Linked List
        https://leetcode.com/problems/reverse-linked-list/description/

        재귀를 통해 링크드 리스트를 역순으로 만든다.

     */

    public ListNode reverseList(ListNode head) {
        return revers(head, null);
    }

    public ListNode revers(ListNode node, ListNode pre) {
        if (node == null) return pre;

        ListNode next = node.next;
        node.next = pre;

        return revers(next, node);
    }
}