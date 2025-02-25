class RemoveNthFromEnd {

  /*
      https://leetcode.com/problems/remove-nth-node-from-end-of-list/
   */

  public ListNode removeNthFromEnd(ListNode head, int n) {
    int size = 0;
    ListNode node = new ListNode(0, head);

    while (node != null) {
      node = node.next;
      size++;
    }

    int i = size - n;

    if (i == 1) {
      return head.next;
    }

    node = new ListNode(0, head);
    while (i-- > 1) {
      node = node.next;
    }

    node.next = node.next.next;

    return head;
  }
}