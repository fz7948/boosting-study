package 장세훈.LeetCode;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class MostCommonWord {
    /*
    819. Most Common Word
    https://leetcode.com/problems/most-common-word/

    입력된 paragraph를 정규식을 통해 단어만 추출한다.
        추출된 단어를 순회를 해 map의 키로 사용하고 value엔 카운팅하며 갯수를 저장한다.
        맵의 value가 가장 큰 키를 반환한다.
 */
    public String mostCommonWord(String paragraph, String[] banned) {
        Map<String, Integer> map = new HashMap<>();
        Set<String> ban = new HashSet<>(Arrays.asList(banned));

        String[] split = paragraph.replaceAll("\\W+", " ").toLowerCase().split(" ");

        for (String s : split) {
            if (!ban.contains(s)) {
                map.put(s, map.getOrDefault(s, 0) + 1);
            }
        }

        return Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}
