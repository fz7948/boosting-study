class OddEvenLinkedList {
    /*
        https://leetcode.com/problems/odd-even-linked-list/
        328. Odd Even Linked List

        주어진 링크드 리스트의 짝수 번째의 노드와 훌수 번째의 노드를 각각 따로 저장
        홀수 노드 끝에 짝수 노드를 붙여주고 반환
     */

    public ListNode oddEvenList(ListNode head) {
        ListNode odd = new ListNode();
        ListNode even = new ListNode();
        ListNode oddHead = odd;
        ListNode evenHead = even;
        int index = 0;
        while(head != null) {
            if(index % 2 != 0) {
                even.next = head;
                even = even.next;
            }else {
                odd.next = head;
                odd = odd.next;
            }
            head = head.next;
            index++;
        }

        even.next = null;
        odd.next = evenHead.next;

        return oddHead.next;
    }
}