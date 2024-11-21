
import java.util.HashMap;
import java.util.Map;

/*
    https://school.programmers.co.kr/learn/courses/30/lessons/42576
    완주하지 못한 선수

    Map의 Key에 participant 문자열, value에 갯수를 넣는다.
    completion 문자열을 map의 key로 사용하며, map에서 조회될 떄 value를 -1 차감한다.
    map의 요소중 value가 0이 아닌 것을 리턴한다.

*/

class 완주하지_못한_선수 {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        String answer="";
        for (String s : participant) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }

        for (String s : completion) {
            map.put(s, map.get(s) - 1);
        }

        for (String s : map.keySet()) {
            if (map.get(s) != 0) {
                answer = s;
                break;
            }
        }

        return answer;
    }
}