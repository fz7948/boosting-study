/*
    https://leetcode.com/problems/merge-k-sorted-lists/submissions/1456002812/
    23. Merge k Sorted Lists

    여러개의 정렬된 링크드 리스트를 입력으로 주짐. 하나의 리스트로 병합하고 오름차순으로 정렬하는 문제.
    
    우선순위 큐를 만들고 각 리스트의 헤더를 넣는다.
    큐에서 노드를 꺼내고, 해당 노드의 다음 노드를 큐에 넣는다.
    큐가 비워질때까지 반복한다.
*/


class MergekSortedLists {

    public static void main(String[] args) {
        new MergekSortedLists().mergeKLists(new ListNode[]{
                new ListNode(1, new ListNode(4, new ListNode(5, null))),
                new ListNode(1, new ListNode(3, new ListNode(4, null))),
                new ListNode(2, new ListNode(7)),
        });
    }

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.val));

        ListNode root = new ListNode(0);
        ListNode tail = root;

        for (ListNode node : lists) {
            if( node != null) pq.add(node);
        }

        while(!pq.isEmpty()) {
            tail.next = pq.poll();
            tail = tail.next;

            if(tail.next != null) pq.add(tail.next);
        }

        return root.next;
    }
}