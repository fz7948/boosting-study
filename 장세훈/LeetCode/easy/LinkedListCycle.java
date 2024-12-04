class LinkedListCycle {
    /*
        141. Linked List Cycle
        https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

        링크드 리스트가 순환하는지 판별하는 문제.
        노드를 순회하며 set에 넣음
        set에 존재하면 true 반환

     */
    public boolean hasCycle(ListNode head) {
        Set<ListNode> set = new HashSet<>();

        while (head != null) {
            set.add(head);
            head = head.next;

            if (set.contains(head))
                return true;
        }

        return false;
    }
}