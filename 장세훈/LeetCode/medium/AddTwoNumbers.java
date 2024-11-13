class AddTwoNumbers {
    /*
        2. Add Two Numbers
        https://leetcode.com/problems/add-two-numbers/description/

        숫자 범위가 너무 크기때문에 단순 덧셈으로 계산이 안됨
        전가산기 개념으로 carry, remainder 변수를 별도로 놓고 덧셈
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode node = new ListNode(0);
        ListNode root = node;

        int sum, carry = 0, remainder;

        while (l1 != null || l2 != null || carry != 0) {
            sum = 0;
            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            remainder = (sum + carry) % 10;
            carry = (sum + carry) / 10;
            node.next = new ListNode(remainder);
            node = node.next;
        }

        return root.next;
    }
}