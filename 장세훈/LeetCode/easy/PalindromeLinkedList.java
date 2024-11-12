class PalindromeLinkedList {

    /*
        234. Palindrome Linked List
        https://leetcode.com/problems/palindrome-linked-list/description/

        링크드 리스트를 순회해 문자열을 만듬
        문자열이 뒤집어도 같은지 확인
     */
    public boolean isPalindrome(ListNode head) {
        String str = "";

        while (head != null) {
            str += head.val;
            head = head.next;
        }

        for (int i = 0; i < str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.length() - 1 - i))
                return false;
        }

        return true;
    }
    
    class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

}