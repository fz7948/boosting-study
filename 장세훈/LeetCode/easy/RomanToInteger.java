class RomanToInteger {

/*
    https://leetcode.com/problems/roman-to-integer/submissions/1553773756/
 */

  public int romanToInt(String s) {
    int answer = 0;
    Map<Character, Integer> map = new HashMap<>();
    map.put('I', 1);
    map.put('V', 5);
    map.put('X', 10);
    map.put('L', 50);
    map.put('C', 100);
    map.put('D', 500);
    map.put('M', 1000);

    for (int i = 0; i < s.length(); i++) {
      if (i < s.length() - 1 && map.get(s.charAt(i)) < map.get(s.charAt(i + 1))) {
        answer -= map.get(s.charAt(i));
      } else {
        answer += map.get(s.charAt(i));
      }
    }

    return answer;
  }
}