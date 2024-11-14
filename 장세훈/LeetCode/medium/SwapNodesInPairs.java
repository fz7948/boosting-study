class SwapNodesInPairs {
    /*
        24. Swap Nodes in Pairs
        https://leetcode.com/problems/swap-nodes-in-pairs/description/

        재귀로 풀이
        링크드 리스트의 노드들을 2개씩 짝으로 순서를 바꾼다.
        재귀를 이용해 노드의 다음 노드를 스왑한 노드로 바꿔준다.
     */


    public ListNode swapPairs(ListNode head) {
        return (head == null || head.next == null) ? head : swap(head);
    }

    public ListNode swap(ListNode node) {
        if (node == null) return null;

        ListNode first = node;
        ListNode second = node.next;
        if (second == null) return first;
        ListNode next = second.next == null ? null : second.next;

        second.next = first;
        first.next =  swap(next);

        return second;
    }
}