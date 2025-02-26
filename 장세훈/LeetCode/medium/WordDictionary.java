class WordDictionary {

    /*
        https://leetcode.com/problems/design-add-and-search-words-data-structure
     */

    Trie root;

    public WordDictionary() {
        root = new Trie();
    }

    public void addWord(String word) {
        Trie t = root;

        for (char c : word.toCharArray()) {
            if (t.next[c - 'a'] == null) {
                t.next[c - 'a'] = new Trie();
            }
            t = t.next[c - 'a'];
        }

        t.isWord = true;
    }

    public boolean search(String word) {
        return find(word.toCharArray(), root, 0);
    }

    private boolean find(char[] word, Trie node, int idx) {
        if (word.length == idx) {
            return node.isWord;
        }

        if (word[idx] == '.') {
            for (int i = 0; i < 26; i++) {
                if (node.next[i] != null) {
                    boolean b = find(word, node.next[i], idx + 1);
                    if (b) return true;
                }
            }
        } else {
            if (node.next[word[idx] - 'a'] != null) {
                return find(word, node.next[word[idx] - 'a'], idx + 1);
            }
        }

        return false;
    }

    static class Trie {
        Trie[] next = new Trie[26];
        boolean isWord = false;
    }
}