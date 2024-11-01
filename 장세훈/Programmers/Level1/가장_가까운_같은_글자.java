package 장세훈.Programmers.Level1;

import java.util.HashMap;
import java.util.Map;

/*
    https://school.programmers.co.kr/learn/courses/30/lessons/142086
    1.문자열을 순회한다
      1-1 Map에서 현재 문자와 위치를 조회한다.
        1-1-1 조회가 되면 answer엔 현 위치에서 조회한 위치를 뺀 값을 넣는다.
        1-1-2 조회가 안되면 answer에 -1을 넣는다.
      1-2 문자와 위치를 Map에 저장한다
      
*/
class 가장_가까운_같은_글자 {
    public int[] solution(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int[] answer = new int[s.length()];

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            answer[i] = map.getOrDefault(c, -1) == -1 ? -1 : i - map.get(c);
            map.put(c, i);
        }

        return answer;
    }
}