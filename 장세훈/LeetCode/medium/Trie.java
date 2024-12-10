class Trie {
    /*
        https://leetcode.com/problems/implement-trie-prefix-tree/
        트라이 구현
    */
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode cur = root;

        for (char c : word.toCharArray()) {
            if (cur.children[c - 'a'] == null)
                cur.children[c - 'a'] = new TrieNode();

            cur = cur.children[c - 'a'];
        }

        cur.word = true;
    }

    public boolean search(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (cur.children[c - 'a'] == null)
                return false;

            cur = cur.children[c - 'a'];
        }

        return cur.word;
    }

    public boolean startsWith(String prefix) {
        TrieNode cur = root;
        for (char c : prefix.toCharArray()) {
            if (cur.children[c - 'a'] == null)
                return false;

            cur = cur.children[c - 'a'];
        }

        return true;
    }

    class TrieNode {
        boolean word;
        TrieNode[] children;

        public TrieNode() {
            children = new TrieNode[26];    // 알파벳 개수만큼 자식 노드 생성
            word = false;
        }
    }
}