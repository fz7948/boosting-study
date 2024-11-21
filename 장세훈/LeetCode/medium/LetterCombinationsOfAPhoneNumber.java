class LetterCombinationsOfAPhoneNumber {
    /*
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
        17. Letter Combinations of a Phone Number

        주어진 숫자로 만들 수 있는 문자 조합을 구하는 문제.
        숫자별 문자들은 map으로 저장.
        bfs 알고리즘으로(재귀) 문자 조합을 만들어 answer에 저장
     */

    Map<Character, List<Character>> map = new HashMap<>();
    List<String> answer = new ArrayList<>();

    void init() {
        map.put('2', List.of('a', 'b', 'c'));
        map.put('3', List.of('d', 'e', 'f'));
        map.put('4', List.of('g', 'h', 'i'));
        map.put('5', List.of('j', 'k', 'l'));
        map.put('6', List.of('m', 'n', 'o'));
        map.put('7', List.of('p', 'q', 'r', 's'));
        map.put('8', List.of('t', 'u', 'v'));
        map.put('9', List.of('w', 'x', 'y', 'z'));

    }

    public List<String> letterCombinations(String digits) {
        if(digits.isEmpty()) return answer;
        init();
        dfs(0, digits, "");
        return answer;
    }

    void dfs(int i, String digits, String str) {
        if (i >= digits.length())
            answer.add(str);
        else {
            List<Character> characters = map.get(digits.charAt(i));
            for (Character character : characters) {
                dfs(i + 1, digits, str + character);
            }
        }
    }
}
